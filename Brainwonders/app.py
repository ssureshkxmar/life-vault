import streamlit as st

st.title("AI-Powered Career Intelligence Platform")

st.sidebar.title("Modules")
module = st.sidebar.selectbox("Select Module", [
    "Career Recommendation",
    "DMIT Dashboard",
    "Roadmap Generator",
    "AI Chatbot",
    "Skill Intelligence"
])

if module == "Career Recommendation":
    st.header("AI Career Recommendation Engine")
    # Import and run the module
    from src.career_recommendation.recommend import main
    main()

elif module == "DMIT Dashboard":
    st.header("Interactive DMIT Dashboard")
    from src.dmit_dashboard.dashboard import main
    main()

elif module == "Roadmap Generator":
    st.header("Career Roadmap Generator")
    from src.roadmap_generator.generator import main
    main()

elif module == "AI Chatbot":
    st.header("AI Counsellor Chatbot")
    from src.counsellor_chatbot.chatbot import main
    main()

elif module == "Skill Intelligence":
    st.header("School/Corporate Skill Intelligence")
    from src.skill_intelligence.intelligence import main
    main()