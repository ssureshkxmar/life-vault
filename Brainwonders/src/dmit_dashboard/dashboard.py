import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

def main():
    st.subheader("📊 Interactive DMIT Dashboard")
    st.write("Comprehensive Brain Dominance & Cognitive Profile Analysis")
    
    # Sample DMIT data
    traits = ['Logical', 'Creative', 'Practical', 'Social', 'Leadership']
    scores = [85, 70, 60, 75, 80]

    # Radar chart
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=scores,
        theta=traits,
        fill='toself',
        name='Your Profile',
        fillcolor='rgba(0, 150, 255, 0.4)',
        line=dict(color='rgb(0, 100, 255)')
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        title="Brain Dominance Profile",
        showlegend=True,
        height=500
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🧠 Brain Dominance")
        left_brain = 75
        right_brain = 65
        st.progress(left_brain / 100, text=f"Left Brain (Analytical): {left_brain}%")
        st.progress(right_brain / 100, text=f"Right Brain (Creative): {right_brain}%")
    
    with col2:
        st.subheader("🎯 Learning Style")
        learning_styles = {
            'Visual': 70,
            'Auditory': 65,
            'Kinesthetic': 80
        }
        for style, score in learning_styles.items():
            st.progress(score / 100, text=f"{style}: {score}%")

    # Career suitability
    st.subheader("🏆 Career Suitability Score")
    careers = ['Data Science', 'Engineering', 'Medicine', 'Arts', 'Research']
    suitability = [90, 85, 70, 60, 88]
    
    df_careers = pd.DataFrame({'Career': careers, 'Suitability': suitability})
    fig_bar = px.bar(df_careers, x='Career', y='Suitability', 
                     color='Suitability', color_continuous_scale='Viridis')
    fig_bar.update_layout(height=400)
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Strengths and Weaknesses
    st.subheader("💪 Strengths & 🎓 Areas for Development")
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Strengths:**")
        st.write("- Excellent logical reasoning")
        st.write("- Strong leadership qualities")
        st.write("- Good practical skills")
    
    with col2:
        st.warning("**Areas for Development:**")
        st.write("- Creative thinking")
        st.write("- Artistic expression")
        st.write("- Social skills enhancement")