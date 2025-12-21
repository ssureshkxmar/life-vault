import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import plotly.graph_objects as go

@st.cache_resource
def load_career_model():
    # Extended dataset
    data = {
        'aptitude_score': [80, 70, 90, 60, 85, 95, 55, 88, 75, 92],
        'interest_score': [75, 80, 85, 65, 90, 92, 60, 87, 78, 91],
        'logical_trait': [85, 60, 90, 40, 80, 95, 35, 88, 70, 93],
        'creative_trait': [60, 90, 50, 80, 70, 40, 85, 55, 88, 45],
        'practical_trait': [70, 75, 80, 75, 75, 70, 70, 78, 72, 75],
        'academic_bg': [85, 78, 92, 70, 88, 94, 65, 90, 80, 96],
        'career': ['Data Science', 'Arts', 'Engineering', 'Trades', 'Medicine', 'Research', 'Hospitality', 'Engineering', 'Commerce', 'Research']
    }
    df = pd.DataFrame(data)
    
    X = df[['aptitude_score', 'interest_score', 'logical_trait', 'creative_trait', 'practical_trait', 'academic_bg']]
    y = df['career']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_scaled, y)
    
    return model, scaler, df

def main():
    st.subheader("🤖 AI Career Recommendation Engine")
    st.write("Get personalized career recommendations based on your aptitude, interests, and DMIT traits.")
    
    model, scaler, df = load_career_model()
    
    col1, col2 = st.columns(2)
    
    with col1:
        aptitude = st.slider("Aptitude Test Score", 0, 100, 75)
        interest = st.slider("Interest Test Score", 0, 100, 80)
        
    with col2:
        logical = st.slider("Logical Thinking", 0, 100, 80)
        creative = st.slider("Creative Thinking", 0, 100, 70)
    
    practical = st.slider("Practical Skills", 0, 100, 75)
    academic = st.slider("Academic Background", 0, 100, 85)
    
    if st.button("🚀 Get Career Recommendations", use_container_width=True):
        # Prepare input
        input_data = np.array([[aptitude, interest, logical, creative, practical, academic]])
        input_scaled = scaler.transform(input_data)
        
        # Get prediction and probabilities
        prediction = model.predict(input_scaled)[0]
        probabilities = model.predict_proba(input_scaled)[0]
        classes = model.classes_
        
        # Sort by probability
        sorted_idx = np.argsort(probabilities)[::-1]
        
        st.success(f"✨ Top Recommended Career: **{prediction}**")
        
        st.subheader("Top 5 Career Matches")
        for i, idx in enumerate(sorted_idx[:5], 1):
            career = classes[idx]
            score = probabilities[idx] * 100
            st.metric(f"{i}. {career}", f"{score:.1f}%")
        
        st.subheader("Why this career?")
        if prediction == "Data Science":
            st.info("Your high logical thinking and aptitude align perfectly with AI/ML field. Strong math foundation needed.")
        elif prediction == "Engineering":
            st.info("Your practical and analytical skills make engineering an excellent fit. Consider specialization.")
        elif prediction == "Medicine":
            st.info("Your consistent performance and dedication suggest medical field. Prepare for competitive exams.")
        else:
            st.info(f"Based on your profile, {prediction} matches your strengths and interests.")