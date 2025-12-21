import streamlit as st

def main():
    st.subheader("🤖 AI Counsellor Chatbot")
    st.write("Get instant answers to your career questions from our AI Counsellor.")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm your AI Counsellor. Ask me anything about careers, aptitude, course selection, or college guidance. How can I help you today?"}
        ]
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # User input
    user_input = st.chat_input("Ask your question...")
    
    if user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Generate AI response
        response = generate_response(user_input)
        
        # Add AI response
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

def generate_response(user_input: str) -> str:
    """Generate response based on user query"""
    user_input_lower = user_input.lower()
    
    # Career recommendation queries
    if any(word in user_input_lower for word in ["career", "job", "profession", "future"]):
        return """Based on your interests and aptitude, here are some career paths to consider:
        
- **Data Science**: Great for analytical minds with strong math skills
- **Engineering**: Perfect for problem solvers
- **Medicine**: Ideal for compassionate and dedicated individuals
- **Business/MBA**: Good for leadership-oriented people
- **Arts/Media**: Best for creative thinkers

Would you like to know more about any specific field?"""
    
    # Stream selection
    elif any(word in user_input_lower for word in ["stream", "subject", "science", "commerce", "arts"]):
        return """Here's my advice on stream selection:
        
**Science**: Choose if you're interested in engineering, medicine, research, or tech
**Commerce**: Best for business, finance, and entrepreneurship
**Arts**: Ideal for humanities, social sciences, and creative fields

Consider your strengths, interests, and career goals. Would you like help deciding?"""
    
    # Exam preparation
    elif any(word in user_input_lower for word in ["exam", "preparation", "study", "preparation"]):
        return """Here are effective exam preparation tips:
        
1. **Create a Study Schedule**: Dedicate 2-3 hours daily
2. **Focus on Weak Areas**: Spend more time on challenging topics
3. **Practice Mock Tests**: Take full-length practice exams
4. **Revision**: Review notes regularly
5. **Stay Healthy**: Get enough sleep and exercise
6. **Join Study Groups**: Learn from peers

Remember: Consistency is key! Would you like subject-specific tips?"""
    
    # Skill development
    elif any(word in user_input_lower for word in ["skill", "develop", "improve", "learn"]):
        return """To develop valuable skills for your career:
        
1. **Technical Skills**: Programming, data analysis, design tools
2. **Soft Skills**: Communication, teamwork, leadership
3. **Online Courses**: Coursera, Udemy, LinkedIn Learning
4. **Projects**: Build real-world projects
5. **Internships**: Gain practical experience
6. **Certifications**: Industry-recognized credentials

What skills are you interested in developing?"""
    
    # College selection
    elif any(word in user_input_lower for word in ["college", "university", "admission", "institution"]):
        return """When choosing a college:
        
1. **Rankings & Reputation**: Check NIRF rankings
2. **Faculty & Resources**: Quality of professors and labs
3. **Placements**: Look at placement statistics
4. **Location & Campus**: Consider your preferences
5. **Course Curriculum**: Ensure relevance to your goals
6. **Fee Structure**: Check affordability

Top colleges: IIT, NIT, BITS, Delhi University, VIT

What field are you looking for?"""
    
    # Default response
    else:
        return """That's an interesting question! Based on current educational trends:
        
- Focus on **STEM fields** for tech-driven future
- Develop **21st-century skills**: Critical thinking, creativity, teamwork
- Don't ignore **soft skills**: Communication and emotional intelligence
- Stay updated with **online learning platforms**
- Gain **real-world experience** through internships

Can you be more specific about what you'd like to know?"""