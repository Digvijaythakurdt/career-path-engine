# 🚀 Universal Career Guidance Engine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/digvijaythakurdt/career-path-engine/main/app.py)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

**An AI-powered application that helps students and job seekers find their ideal career path based on skills, experience, and market trends.**

---

## 🖼️ Project Preview

![Dashboard Preview](https://github.com/digvijaythakurdt/career-path-engine/blob/main/dashboard.png?raw=true)
--(Note: Upload a screenshot named `dashboard.png` to your repo to see the preview here)

---

## 💡 What is this?
The **Universal Career Guidance Engine** is a machine learning-based tool designed to bridge the gap between technical skills and job market requirements. It analyzes a user's skill set (e.g., Python, SQL, Selenium) and predicts the most suitable job role with a confidence score.

It also provides **real-time market insights**, salary estimations based on location/experience, and actionable advice to help candidates upskill.

## 🌟 Key Features
* **🤖 AI Career Prediction:** Uses a **Random Forest Classifier** with TF-IDF vectorization to predict roles like *Data Scientist, QA Engineer, Web Developer*, etc.
* **📊 Interactive Market Insights:** Visualizes job demand and salary trends using **Plotly** and **Matplotlib**.
* **💰 Dynamic Salary Engine:** Estimates salary packages (LPA) based on city (e.g., Pune vs. Mumbai), experience level, and role complexity.
* **🎨 Professional UI:** Features a custom Dark Theme with brand-aligned primary colors.
* **📝 Smart Recommendations:** Provides specific advice (e.g., "Learn Figma" for UI/UX or "Master SQL" for Analysts) based on the prediction.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **Machine Learning:** Scikit-Learn (Random Forest, Pipeline)
* **Data Processing:** Pandas, NumPy
* **Visualization:** Plotly Express, Matplotlib
* **Deployment:** Streamlit Cloud

## 📂 Project Structure
```bash
├── app.py                   # The main application code
├── universal_job_data.csv   # Dataset used for training the model
├── requirements.txt         # List of dependencies for deployment
├── .streamlit/
│   └── config.toml          # Custom theme configuration (Dark Mode & Green Accent)
└── README.md                # Project documentation
