import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Universal Career Advisor", layout="wide")

# --- LOAD DATA & TRAIN MODEL ---
@st.cache_resource
def load_and_train_model():
    try:
        # Load the NEW Universal Dataset
        df = pd.read_csv('universal_job_data.csv')
    except FileNotFoundError:
        st.error("CSV file not found. Please run 'generate_data.py' first.")
        return None, None

    # Pipeline: Text -> Vectors -> Random Forest Classifier
    model = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', RandomForestClassifier(n_estimators=100))
    ])
    
    model.fit(df['Skills'], df['Role'])
    return model, df

model, df = load_and_train_model()

# --- SIDEBAR INPUTS ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
st.sidebar.title("👨‍💻 Profile Setup")

user_skills = st.sidebar.text_area("Enter your Skills", "Java, Selenium, JIRA")
user_exp = st.sidebar.slider("Years of Experience", 0, 10, 0)
user_city = st.sidebar.selectbox("Preferred City", ["Pune", "Mumbai", "Bangalore", "Hyderabad", "Remote"])

# Button with primary type (Green if you have the config file)
predict_btn = st.sidebar.button("🚀 Analyze Career Path", type="primary")

# --- MAIN DASHBOARD ---
st.title("🧭 Universal Career Guidance Engine")
st.markdown("#### AI-Powered Path Finder for Students & Job Seekers")

# Create layout for Prediction
col_pred1, col_pred2 = st.columns([2, 1])

with col_pred1:
    if predict_btn and model:
        # 1. Predict Role
        prediction = model.predict([user_skills])[0]
        probs = model.predict_proba([user_skills])
        confidence = np.max(probs) * 100

        st.success(f"### 🎯 Recommended Career: {prediction}")
        
        # --- CONFIDENCE SCORE ---
        st.markdown(f"""
            <div style="background-color: #d1e7dd; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
                <p style="font-size: 18px; margin: 0; color: #0f5132;">Model Confidence</p>
                <p style="font-size: 45px; font-weight: bold; margin: 0; color: #198754;">
                    {confidence:.1f}%
                </p>
            </div>
        """, unsafe_allow_html=True)

        # 2. Dynamic Salary Logic
        base_salary = 3.0 # Base for freshers
        
        if "Scientist" in prediction: base_salary = 6.0
        elif "Developer" in prediction: base_salary = 4.5
        elif "UI/UX" in prediction: base_salary = 4.0
        elif "QA" in prediction: base_salary = 3.5
        elif "Analyst" in prediction: base_salary = 4.0
        
        if user_city in ["Mumbai", "Bangalore"]: base_salary += 1.5
        final_salary = base_salary + (user_exp * 1.5)
        
        st.info(f"💰 **Estimated Salary:** ₹{final_salary:.1f} LPA - ₹{final_salary+3.0:.1f} LPA")
        
        # 3. Specific Career Advice
        st.markdown("---")
        st.subheader("💡 Expert Advice for this Stream")
        
        if "UI/UX" in prediction:
            st.warning("🎨 **Portfolio Tip:** Recruiters look for Behance/Dribbble links. Learn **Figma** components deeply.")
        elif "QA" in prediction:
            st.warning("🐞 **Pro Tip:** Automation is the future. If you know Manual Testing, start learning **Selenium with Python/Java** immediately.")
        elif "Web" in prediction:
            st.warning("💻 **Dev Tip:** Learn a modern framework like **React** or **Angular**. Plain HTML/CSS is not enough anymore.")
        elif "Data" in prediction:
            st.warning("📊 **Analyst Tip:** Master **SQL**. It is the most asked skill in interviews, even more than Python.")
            
    elif not predict_btn:
        st.info("👈 Enter your skills (e.g., 'Figma, CSS' or 'Java, SQL') in the sidebar to start!")

with col_pred2:
    if df is not None:
        st.subheader("📊 Market Distribution")
        role_counts = df['Role'].value_counts()
        st.bar_chart(role_counts)
        st.caption("Distribution of Jobs in our AI Database")


# --- MARKET INSIGHTS SECTION ---
# Sample data for charts
data = {
    'Role': ['Data Scientist', 'Data Analyst', 'QA Engineer', 'Software Dev', 'DE'],
    'Demand_Score': [85, 90, 65, 95, 70],
    'Avg_Salary_LPA': [14.5, 8.5, 6.0, 12.0, 15.0],
    'Open_Positions': [120, 200, 80, 300, 90]
}
df_chart = pd.DataFrame(data)

st.markdown("---")
st.header("📊 Market Insights & Trends")

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Job Market Demand")
    fig_demand = px.bar(
        df_chart, 
        x='Role', 
        y='Demand_Score', 
        color='Role',
        color_discrete_sequence=px.colors.qualitative.Pastel,
        title="Demand Score by Role"
    )
    fig_demand.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    # FIXED: Removed 'use_container_width' warning
    st.plotly_chart(fig_demand)

with col_chart2:
    st.subheader("Salary Estimator (LPA)")
    fig_salary = px.bar(
        df_chart, 
        x='Role', 
        y='Avg_Salary_LPA', 
        text='Avg_Salary_LPA',
        color='Avg_Salary_LPA',
        color_continuous_scale='Greens',
        title="Average Salary Package"
    )
    fig_salary.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    # FIXED: Removed 'use_container_width' warning
    st.plotly_chart(fig_salary)

# --- DATAFRAME SUMMARY ---
with st.expander("🔎 View Detailed Data Table"):
    # This requires 'pip install matplotlib'

    st.dataframe(df_chart.style.background_gradient(cmap="Greens"))

st.sidebar.markdown("---")
st.sidebar.caption("© 2025 | Developed by **Digvijay Ganesh Thakur**")
