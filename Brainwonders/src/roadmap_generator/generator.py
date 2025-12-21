import streamlit as st

def main():
    st.subheader("🗺️ Career Roadmap Generator")
    st.write("Get a personalized career development plan with milestones and skills.")
    
    career = st.selectbox("Select Career Path", [
        "Data Scientist",
        "Medical Doctor",
        "Software Engineer",
        "Civil Engineer",
        "Business Analyst",
        "Research Scientist",
        "Graphic Designer"
    ])

    if st.button("📋 Generate Your Roadmap", use_container_width=True):
        roadmaps = {
            "Data Scientist": {
                "stages": [
                    ("Class 8-10", "Strengthen Math & Science Foundation", ["Mathematics", "Physics", "Chemistry", "Computer Basics"]),
                    ("Class 11-12", "PCM with Computer Science", ["Advanced Math", "Programming", "Problem Solving"]),
                    ("Graduation", "B.Tech in CSE/Statistics (4 years)", ["Python", "SQL", "Statistics", "Linear Algebra"]),
                    ("Post-Grad", "M.Tech/Masters (2 years)", ["Machine Learning", "Deep Learning", "NLP"]),
                    ("Professional", "Industry Experience (1-3 years)", ["Production ML", "Data Engineering", "Cloud Platforms"])
                ],
                "duration": "8-10 years",
                "skills": ["Python", "R", "SQL", "TensorFlow", "Pandas", "Scikit-Learn", "Cloud", "Docker"]
            },
            "Medical Doctor": {
                "stages": [
                    ("Class 8-10", "Strengthen Science Foundation", ["Biology", "Chemistry", "Physics"]),
                    ("Class 11-12", "PCB Stream", ["Advanced Biology", "Organic Chemistry", "Anatomy"]),
                    ("NEET Prep", "Competitive Exam Preparation (1 year)", ["NEET Coaching", "Mock Tests"]),
                    ("Medical School", "MBBS (5.5 years)", ["Clinical Practice", "Internship"]),
                    ("Specialization", "MD/MS (3 years)", ["Advanced Medical Knowledge", "Surgery/Medicine"])
                ],
                "duration": "10-12 years",
                "skills": ["Clinical Skills", "Diagnosis", "Research", "Communication"]
            },
            "Software Engineer": {
                "stages": [
                    ("Class 8-10", "Computer Fundamentals", ["Programming Basics", "Algorithms", "Data Structures"]),
                    ("Class 11-12", "PCM with CS", ["Advanced Programming", "Web Basics"]),
                    ("Graduation", "B.Tech CSE (4 years)", ["Core CS Subjects", "Project Development"]),
                    ("Internships", "Work Experience (1-2 years)", ["Real Projects", "Team Collaboration"]),
                    ("Professional", "Senior Development (3+ years)", ["System Design", "Leadership", "Architecture"])
                ],
                "duration": "6-8 years",
                "skills": ["Java", "Python", "JavaScript", "React", "System Design", "Git", "AWS", "Docker"]
            }
        }
        
        if career in roadmaps:
            roadmap = roadmaps[career]
            
            st.success(f"### Your {career} Roadmap")
            st.info(f"**Total Timeline:** {roadmap['duration']}")
            
            st.subheader("📍 Milestone Stages")
            for i, (stage, description, skills) in enumerate(roadmap["stages"], 1):
                with st.expander(f"Stage {i}: {stage}"):
                    st.write(f"**{description}**")
                    st.write("**Key Skills:**")
                    for skill in skills:
                        st.write(f"• {skill}")
            
            st.subheader("👨‍🎓 Core Skills to Master")
            cols = st.columns(3)
            for i, skill in enumerate(roadmap["skills"]):
                with cols[i % 3]:
                    st.success(skill)
        else:
            st.info(f"Roadmap for {career} coming soon!")