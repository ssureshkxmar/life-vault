import streamlit as st
import requests

# Cloudflare AI Configuration
CLOUDFLARE_ACCOUNT_ID = "beb7787ed2562d195ccdd4d66f8c4e70"
CLOUDFLARE_API_TOKEN = "cfat_OOu4fRUw9fJRat5Eji88fBFVzmJH95QStNIrgoMI52efb3d0"
MODEL_ID = "@cf/meta/llama-3-8b-instruct"

def main():
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm your Life Vault Specialist. How can I help you navigate your personalized career roadmap today?"}
        ]
    
    # Smaller height for compact feel
    chat_container = st.container(height=350, border=True)
    
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    user_input = st.chat_input("Ask about your report...")
    
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with chat_container:
            with st.chat_message("user"):
                st.markdown(user_input)
            
            with st.spinner("Analyzing Vault Data..."):
                # Get report context if available
                context = ""
                if st.session_state.get('report_generated'):
                    inputs = st.session_state.student_inputs
                    context = f"The student is named {inputs.get('name')}, age {inputs.get('age')}. "
                    context += f"Scores: Aptitude:{inputs.get('aptitude')}, Logical:{inputs.get('logical')}, Creative:{inputs.get('creative')}. "
                    # We might not have predicted_career here easily, but we can assume common sense
                
                response = generate_ai_response(st.session_state.messages, context)
            
            if response:
                st.session_state.messages.append({"role": "assistant", "content": response})
                with chat_container:
                    with st.chat_message("assistant"):
                        st.markdown(response)
            else:
                st.error("Vault connection timeout.")

def generate_ai_response(messages, context="") -> str:
    """Generate response using Cloudflare Workers AI"""
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/{MODEL_ID}"
    headers = {"Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}"}
    
    system_content = "You are the 'Life Vault AI Specialist'. You provide elite, precise career guidance. "
    if context:
        system_content += f"STUDENT CONTEXT: {context}. Use this data to provide hyper-personalized explanations about their report and milestones."
    
    system_prompt = {"role": "system", "content": system_content}
    
    payload = {
        "messages": [system_prompt] + messages,
        "stream": False
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.status_code == 200:
            result = response.json()
            return result["result"]["response"]
        return None
    except Exception:
        return None