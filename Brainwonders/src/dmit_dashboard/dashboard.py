import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

def render_dmit_dashboard(logical_score, creative_score, practical_score):
    st.markdown("<h2 class='main-title'>Interactive <span>DMIT Dashboard</span></h2>", unsafe_allow_html=True)
    st.write("Comprehensive Brain Dominance & Cognitive Profile Analysis based on your inputs.")
    
    # DMIT data using actual inputs + some static derivations
    traits = ['Logical', 'Creative', 'Practical', 'Social', 'Leadership']
    scores = [logical_score, creative_score, practical_score, 75, 80]

    # Radar chart in light professional theme
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=scores,
        theta=traits,
        fill='toself',
        name='Your Profile',
        marker=dict(color='#2563eb'),
        fillcolor='rgba(37, 99, 235, 0.2)',
        line=dict(color='#2563eb', width=2)
    ))
    fig_radar.update_layout(
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor="rgba(0,0,0,0.1)"),
            angularaxis=dict(gridcolor="rgba(0,0,0,0.1)")
        ),
        title=dict(text="Brain Dominance Profile", font=dict(size=20, color="#0f172a")),
        showlegend=False,
        height=450
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🧠 Brain Dominance")
        left_brain = int((logical_score + practical_score) / 2)
        right_brain = int(creative_score)
        st.progress(left_brain / 100, text=f"Left Brain (Analytical): {left_brain}%")
        st.progress(right_brain / 100, text=f"Right Brain (Creative): {right_brain}%")
    
    with col2:
        st.markdown("### 🎯 Learning Style")
        learning_styles = {
            'Visual': 70,
            'Auditory': 65,
            'Kinesthetic': 80
        }
        for style, score in learning_styles.items():
            st.progress(score / 100, text=f"{style}: {score}%")

    # Career suitability
    st.markdown("### 🏆 Career Suitability Score")
    careers = ['Data Science', 'Engineering', 'Medicine', 'Arts', 'Research']
    suitability = [logical_score + 5, practical_score + 10, 70, creative_score, 88]
    
    df_careers = pd.DataFrame({'Career': careers, 'Suitability': suitability})
    fig_bar = px.bar(df_careers, x='Career', y='Suitability', 
                     color='Suitability', color_continuous_scale=['#4f46e5', '#3b82f6', '#2563eb'])
    fig_bar.update_layout(
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=350,
        xaxis=dict(gridcolor="rgba(0,0,0,0.05)", title_font=dict(color="#0f172a"), tickfont=dict(color="#475569")),
        yaxis=dict(gridcolor="rgba(0,0,0,0.05)", title_font=dict(color="#0f172a"), tickfont=dict(color="#475569"))
    )
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