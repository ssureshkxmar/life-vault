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

def render_recommendations(aptitude, interest, logical, creative, practical, academic):
    st.markdown("<h2 class='main-title'>AI <span>Career Recommendation Engine</span></h2>", unsafe_allow_html=True)
    st.write("Personalized career recommendations based on your aptitude, interests, and DMIT traits.")
    
    model, scaler, df = load_career_model()
    
    # Prepare input
    input_data = np.array([[aptitude, interest, logical, creative, practical, academic]])
    input_scaled = scaler.transform(input_data)
    
    # Get prediction and probabilities
    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]
    classes = model.classes_
    
    # Sort by probability
    sorted_idx = np.argsort(probabilities)[::-1]
    
    # Beautiful Massive Trophy Banner for Top Career
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #2563eb, #4f46e5); padding: 40px; border-radius: 20px; text-align: center; color: white; box-shadow: 0 10px 30px rgba(37,99,235,0.3); margin-bottom: 30px;">
            <p style="font-size: 1.2rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; font-weight: 500;">Your Master AI Prediction</p>
            <h1 style="font-size: 3.5rem; font-weight: 800; color: white; margin: 0; display: flex; align-items: center; justify-content: center; gap: 15px;">
                🏆 {prediction}
            </h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 style="color: #0f172a; margin-bottom: 15px;">Top 5 Synergistic Matches</h3>', unsafe_allow_html=True)
    cols = st.columns(5)
    for i, idx in enumerate(sorted_idx[:5]):
        career = classes[idx]
        score = probabilities[idx] * 100
        cols[i].metric(f"#{i+1} {career}", f"{score:.1f}%")
    
    # Beautiful Why this career box
    reason = f"Based on our deep cognitive analysis, {prediction} flawlessly synergizes with your assessed traits and interests."
    if prediction == "Data Science":
        reason = "Your high logical thinking and aptitude perfectly match the rigorous analytical demands of the AI/ML industry."
    elif prediction == "Engineering":
        reason = "Your practical, solution-oriented mind and analytical skills make Engineering an extraordinary fit."
    elif prediction == "Medicine":
        reason = "Your consistent academic performance and deep dedication heavily suggest high success in the Medical field."
    elif prediction == "Commerce":
        reason = "Your balanced logic and strong practical skills position you perfectly for financial leadership and business strategy."
        
    st.markdown(f"""
        <div style="background: #f1f5f9; border-left: 5px solid #2563eb; padding: 25px; border-radius: 0 15px 15px 0; margin-top: 30px;">
            <h4 style="color: #1e293b; margin: 0 0 10px 0;">Why this career?</h4>
            <p style="color: #475569; font-size: 1.1rem; margin: 0;">{reason}</p>
        </div>
    """, unsafe_allow_html=True)
        
    return prediction