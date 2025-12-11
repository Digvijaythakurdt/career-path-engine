import pandas as pd
import random

# Define the "Archetypes" - what these roles actually look like
job_archetypes = {
    "Data Scientist": [
        "Python, SQL, Machine Learning, Pandas", "R, Deep Learning, NLP, Python",
        "Python, Spark, AWS, Statistics", "TensorFlow, Keras, Python, SQL"
    ],
    "Data Analyst": [
        "Excel, SQL, Power BI, Tableau", "Python, SQL, Excel, Visualization",
        "Tableau, SQL, Communication, Statistics", "Excel, VBA, SQL, Python"
    ],
    "Software Developer": [
        "Java, Spring Boot, SQL, Microservices", "C++, STL, Algorithms, Linux",
        "C#, .NET, Azure, SQL Server", "Java, Hibernate, REST API, Git"
    ],
    "Web Developer": [
        "HTML, CSS, JavaScript, React", "Node.js, Express, MongoDB, React",
        "Angular, TypeScript, HTML, CSS", "PHP, Laravel, MySQL, JavaScript"
    ],
    "UI/UX Designer": [
        "Figma, Adobe XD, Sketch, Wireframing", "Photoshop, Illustrator, CSS, HTML",
        "User Research, Prototyping, Figma, UI Design", "Adobe Creative Suite, Wireframing, UX Principles"
    ],
    "QA Engineer": [
        "Selenium, Java, TestNG, JIRA", "Manual Testing, SQL, API Testing, Postman",
        "Python, PyTest, Automation, Linux", "Cypress, JavaScript, QA, Agile"
    ]
}

cities = ["Pune", "Mumbai", "Bangalore", "Hyderabad", "Remote"]

data = []

# Generate 1000 rows of diverse data
print("Generating synthetic real-world data...")
for _ in range(1000):
    role = random.choice(list(job_archetypes.keys()))
    skills = random.choice(job_archetypes[role])
    
    exp = random.randint(0, 8)
    city = random.choice(cities)
    exp_str = f"{exp} - {exp+2} yrs" if random.random() > 0.2 else f"{exp}+ years"
    
    data.append({
        "Role": role,
        "Company": "Tech Corp",
        "Skills": skills,
        "Experience": exp_str,
        "Location": city
    })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('universal_job_data.csv', index=False)
print(f"SUCCESS: Generated 'universal_job_data.csv' with {len(df)} rows.")