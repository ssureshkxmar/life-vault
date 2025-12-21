import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def main():
    st.subheader("📈 School/Corporate Skill Intelligence")
    
    tab1, tab2 = st.tabs(["🏫 School Analytics", "💼 Corporate Analytics"])
    
    with tab1:
        st.subheader("School-Wide Intelligence Dashboard")
        
        # Class-wise aptitude heatmap
        data_class = {
            'Class': ['8', '9', '10', '11', '12'],
            'Avg_Aptitude': [70, 75, 80, 78, 85],
            'Student_Count': [45, 48, 50, 52, 48]
        }
        df_class = pd.DataFrame(data_class)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_bar = px.bar(df_class, x='Class', y='Avg_Aptitude',
                           title="Class-wise Aptitude Trend",
                           color='Avg_Aptitude',
                           color_continuous_scale='Viridis')
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with col2:
            fig_students = px.bar(df_class, x='Class', y='Student_Count',
                                title="Student Distribution",
                                color='Student_Count',
                                color_continuous_scale='Blues')
            st.plotly_chart(fig_students, use_container_width=True)
        
        # Subject strength analysis
        st.subheader("Subject Strength Analysis")
        subjects_data = {
            'Subject': ['Math', 'Science', 'English', 'Social Studies', 'Computers'],
            'Avg_Score': [72, 78, 65, 70, 82],
            'Improvement_Rate': [5, 8, 12, 6, 15]
        }
        df_subjects = pd.DataFrame(subjects_data)
        
        fig_subjects = px.scatter(df_subjects, x='Subject', y='Avg_Score',
                                 size='Improvement_Rate',
                                 color='Avg_Score',
                                 color_continuous_scale='Plasma',
                                 title="Subject Performance & Improvement")
        st.plotly_chart(fig_subjects, use_container_width=True)
        
        # Career distribution
        st.subheader("Career Interest Distribution (Class 12)")
        careers_interest = {
            'Career': ['Science', 'Engineering', 'Medical', 'Commerce', 'Arts', 'Other'],
            'Students': [15, 18, 12, 8, 8, 5]
        }
        df_careers = pd.DataFrame(careers_interest)
        
        fig_pie = px.pie(df_careers, values='Students', names='Career',
                        title="Student Career Preferences")
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with tab2:
        st.subheader("Corporate Skill Gap & Training Analysis")
        
        # Skill gap analysis
        col1, col2 = st.columns(2)
        
        with col1:
            skills_gap = {
                'Skill': ['Python', 'ML/AI', 'Cloud', 'Communication', 'Leadership', 'Data Analysis'],
                'Gap_Percentage': [20, 35, 25, 15, 18, 22]
            }
            df_skills = pd.DataFrame(skills_gap)
            
            fig_gap = px.bar(df_skills, x='Skill', y='Gap_Percentage',
                           title="Skill Gap Analysis",
                           color='Gap_Percentage',
                           color_continuous_scale='Reds')
            st.plotly_chart(fig_gap, use_container_width=True)
        
        with col2:
            # Employee proficiency levels
            proficiency_data = {
                'Level': ['Expert', 'Intermediate', 'Beginner', 'No Experience'],
                'Count': [45, 78, 52, 25]
            }
            df_proficiency = pd.DataFrame(proficiency_data)
            
            fig_prof = px.pie(df_proficiency, values='Count', names='Level',
                             title="Employee Proficiency Distribution",
                             hole=0.3)
            st.plotly_chart(fig_prof, use_container_width=True)
        
        # Training recommendations
        st.subheader("Training Recommendations")
        recommendations = [
            ("Python Programming", "High Priority", "35% employees below target"),
            ("ML/AI Fundamentals", "High Priority", "Critical for innovation"),
            ("Cloud Technologies", "Medium Priority", "AWS/Azure certification"),
            ("Leadership Skills", "Medium Priority", "For 50+ senior employees"),
            ("Data Analysis", "Medium Priority", "30+ employees need upskilling")
        ]
        
        for training, priority, reason in recommendations:
            if priority == "High Priority":
                st.error(f"**{training}** - {priority}")
                st.write(f"Reason: {reason}")
            else:
                st.warning(f"**{training}** - {priority}")
                st.write(f"Reason: {reason}")
            st.divider()