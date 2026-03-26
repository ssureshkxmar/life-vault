import streamlit as st

def render_roadmap(career):
    st.markdown("<h2 class='main-title'>Life <span>Roadmap Vault</span></h2>", unsafe_allow_html=True)
    st.write(f"Secure your lifetime career success with this custom roadmap for **{career}**.")
    
    roadmaps = {
        "Data Science": {
            "stages": [
                ("Class 8-10", "Foundation", "Develop deep mathematical and computer science foundations."),
                ("Class 11-12", "Specialization", "Master PCM with a focus on advanced logic and algorithms."),
                ("Graduation", "Core Degree", "B.Tech CSE/Statistics focus on Python, SQL, and Data Modeling."),
                ("Post-Grad", "Advanced AI", "Specialization in Machine Learning, Deep Learning, and NLP."),
                ("Professional", "Elite Lead", "Industry lead role in Production AI and Data Governance.")
            ],
            "duration": "8-10 years",
            "skills": ["Python", "TensorFlow", "Pandas", "Cloud Architecture"]
        },
        "Medicine": {
            "stages": [
                ("Class 8-10", "Science Prep", "Biology and Chemistry excellence."),
                ("Class 11-12", "PCB Excellence", "Targeting 95%+ in Biology and NEET preparation."),
                ("Medical School", "MBBS", "5.5 years of intensive clinical and anatomical study."),
                ("Specialization", "MD/MS", "Mastery of specialized surgery or general medicine."),
                ("Professional", "Senior Surgeon", "Clinical leadership and advanced research.")
            ],
            "duration": "10-12 years",
            "skills": ["Clinical Diagnosis", "Surgical Precision", "Patient Ethics"]
        },
        "Engineering": {
            "stages": [
                ("Class 8-10", "Logic Basics", "Algorithmic thinking and basic scripting."),
                ("Class 11-12", "Tech Stream", "PCM focus with early web and software projects."),
                ("Graduation", "B.Tech", "Full-stack development, OS fundamentals, and AI basics."),
                ("Professional", "DevOps/Dev", "Deployment, CI/CD, and Senior Engineering roles."),
                ("Leadership", "CTO", "Strategic technical leadership and system design.")
            ],
            "duration": "6-8 years",
            "skills": ["System Design", "Cloud Native", "GitOps", "Python/Java"]
        },
        "Commerce": {
            "stages": [
                ("Class 8-10", "Basic Economics", "Understanding fundamentals of finance and math."),
                ("Class 11-12", "Commerce Opts", "Accountancy, Business Studies, and early finance."),
                ("Graduation", "B.Com/BBA", "Corporate law, taxation, and financial management."),
                ("License", "CA/CFA", "Elite professional certification and strategic auditing."),
                ("Leadership", "Finance Director", "Leading global investment and corporate strategy.")
            ],
            "duration": "5-8 years",
            "skills": ["Strategic Finance", "Corporate Law", "Audit Excellence"]
        }
    }
    
    # Fallback mappings for slightly different job titles
    mapped_career = career
    if "Data" in career: mapped_career = "Data Science"
    elif "Med" in career: mapped_career = "Medicine"
    elif "Eng" in career or "Arts" in career or "Research" in career: mapped_career = "Engineering" 
    elif "Commerce" in career or "Finance" in career or "Business" in career: mapped_career = "Commerce"
    
    if mapped_career in roadmaps:
        roadmap = roadmaps[mapped_career]
        
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f0fdf4, #ffffff); border: 1px solid #d1fae5; padding: 25px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.02); margin-top: 20px;">
                <h3 style="color: #065f46; margin-bottom: 5px;">📍 Life Milestone Timeline: {career}</h3>
                <p style="color: #059669; font-weight: 600;">Total Safe Timeline: {roadmap['duration']}</p>
            </div>
        """, unsafe_allow_html=True)

        for i, (stage, title, desc) in enumerate(roadmap["stages"], 1):
            st.markdown(f"""
                <div style="display: flex; gap: 20px; align-items: flex-start; margin: 20px 0;">
                    <div style="background: #10b981; color: white; min-width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.1rem; box-shadow: 0 4px 10px rgba(16,185,129,0.3);">{i}</div>
                    <div style="background: white; border: 1px solid #e2e8f0; padding: 20px; border-radius: 16px; flex-grow: 1; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">
                        <h4 style="margin: 0; color: #1e293b; font-size: 1.1rem;">{stage}: <span style="color: #10b981;">{title}</span></h4>
                        <p style="margin: 8px 0 0 0; color: #64748b; font-size: 0.95rem;">{desc}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<h4 style='color: #1e293b; margin-top: 30px;'>🎯 Master Skills to Vault</h4>", unsafe_allow_html=True)
        cols = st.columns(4)
        for i, skill in enumerate(roadmap["skills"]):
            cols[i % 4].markdown(f"""
                <div style="background: #f0f9ff; border: 1px solid #bae6fd; padding:12px; border-radius: 12px; text-align: center; font-weight: 600; color: #0369a1; font-size: 0.9rem;">{skill}</div>
            """, unsafe_allow_html=True)
    else:
        st.info(f"Roadmap for {career} coming soon!")