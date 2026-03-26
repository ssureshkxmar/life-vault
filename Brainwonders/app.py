import streamlit as st
import streamlit.components.v1 as components

# 1. Advanced Page Configuration
st.set_page_config(
    page_title="Life Vault | Secure Career Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Professional Enterprise CSS Injection
st.markdown("""
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Outfit', sans-serif !important;
    }

    /* Main App Background */
    .stApp {
        background: #f8fafc;
    }

    /* Custom Header Styling - Removes default white bar top padding */
    header[data-testid="stHeader"] {
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(8px);
        border-bottom: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
    }

    /* Floating Navigation (Sidebar) */
    [data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 1px solid #e2e8f0;
        box-shadow: 1px 0 15px rgba(0,0,0,0.02);
    }

    /* Sidebar Content Typography */
    .sidebar-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #2563eb;
        margin-bottom: 20px;
        text-align: center;
        letter-spacing: -0.5px;
    }

    /* Stat/Metric Cards */
    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        transition: all 0.3s ease;
    }
    div[data-testid="stMetric"]:hover {
        border-color: #2563eb;
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    div[data-testid="stMetric"] label {
        color: #64748b !important;
        font-weight: 500;
    }

    /* Title Gradient */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: #0f172a;
        text-align: left;
        margin-bottom: 0px;
        letter-spacing: -1.5px;
    }
    .main-title span {
        color: #2563eb;
        font-weight: 600;
    }

    /* Sidebar Selectbox Custom Style */
    .stSelectbox div[data-baseweb="select"] {
        background: #f1f5f9;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        color: #0f172a;
    }
    .stSelectbox label {
        color: #475569 !important;
        font-weight: 600;
    }

    /* Button Styling */
    button[kind="primary"] {
        background: #2563eb !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 8px 20px !important;
        border: none !important;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2) !important;
        transition: all 0.2s ease !important;
    }
    button[kind="primary"]:hover {
        background: #1d4ed8 !important;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3) !important;
        transform: translateY(-2px) !important;
    }
    
    button[kind="secondary"] {
        background: #ffffff !important;
        color: #0f172a !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        border: 1px solid #e2e8f0 !important;
        transition: all 0.2s ease !important;
    }
    button[kind="secondary"]:hover {
        border-color: #2563eb !important;
        color: #2563eb !important;
    }

    /* Overriding Streamlit text colors globally for light theme */
    .stMarkdown p, .stMarkdown li, .stMarkdown div {
        color: #334155 !important;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: #0f172a !important;
    }

    /* Hide Built-in Streamlit elements */
    /* Hide Built-in Streamlit elements across ALL versions */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    [data-testid="stHeader"] {visibility: hidden !important;}
    [data-testid="stAppViewBlockContainer"] header {visibility: hidden !important;}
    .stDeployButton {visibility: hidden !important;}
    #stDecoration {visibility: hidden !important;}
    
    /* Attractive Form Card */
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(37, 99, 235, 0.2) !important;
        border-radius: 24px !important;
        padding: 40px !important;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05) !important;
    }

    /* Input Field Styling */
    div[data-baseweb="input"] {
        background: #f8fafc !important;
        border-radius: 10px !important;
    }

    /* Slider Styling */
    div[data-testid="stSlider"] label {
        color: #1e293b !important;
        font-weight: 600 !important;
    }

    /* Printing Overrides */
    @media print {
        .stButton, .stChatInput, header, footer, #MainMenu, [data-testid="stSidebar"], .stChatFloatingInput {
            display: none !important;
        }
        .stApp {
            background: white !important;
            padding: 0 !important;
        }
        .main-title, h1, h2, h3, h4 {
            color: black !important;
        }
        div[data-testid="stMetric"] {
            border: 1px solid #ddd !important;
            box-shadow: none !important;
        }
    }

    /* Iframe padding reduction */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 5rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Handle User Context from Frontend
query_params = st.query_params
user_name_ext = query_params.get("name", "Student")
if isinstance(user_name_ext, list):
    user_name_ext = user_name_ext[0] if user_name_ext else "Student"

if 'report_generated' not in st.session_state:
    st.session_state.report_generated = False
    st.session_state.student_inputs = {}

# 4. Single-Page Master Form
if not st.session_state.report_generated:
    st.markdown(f'<h1 class="main-title">Hey! Welcome to <span>Life Vault</span> Analysis for <span>{user_name_ext}</span></h1>', unsafe_allow_html=True)
    st.write("Fill in your assessment scores below to instantly generate a full career, cognitive, and skill analysis.")
    
    with st.form("student_analysis_form", border=True):
        st.markdown("### 📋 Student Information")
        colA, colB, colC = st.columns(3)
        with colA:
            name_input = st.text_input("Student Name", value=user_name_ext)
        with colB:
            age = st.number_input("Student Age", min_value=5, max_value=25, value=15)
        with colC:
            attendance = st.slider("Attendance %", 0, 100, 90)
            
        st.markdown("---")
        st.markdown("### 🧪 Cognitive & Assessment Scores")
        col1, col2 = st.columns(2)
        with col1:
            aptitude = st.slider("Aptitude Test Score", 0, 100, 75)
            interest = st.slider("Interest Test Score", 0, 100, 80)
            logical = st.slider("Logical Thinking", 0, 100, 80)
        with col2:
            creative = st.slider("Creative Thinking", 0, 100, 70)
            practical = st.slider("Practical Skills", 0, 100, 75)
            academic = st.slider("Academic Background", 0, 100, 85)
            
        submit = st.form_submit_button("Analysis", type="primary")
        if submit:
            st.session_state.report_generated = True
            st.session_state.student_inputs = {
                'name': name_input,
                'age': age,
                'attendance': attendance,
                'aptitude': aptitude,
                'interest': interest,
                'logical': logical,
                'creative': creative,
                'practical': practical,
                'academic': academic
            }
            st.rerun()

else:
    inputs = st.session_state.student_inputs
    
    # Report Header with Company Logo
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("assets/logo.png", width=128)
    with col2:
        st.markdown(f'<div style="font-size: 1.8rem; font-weight: 800; color: #2563eb; margin-bottom: -10px;">LIFE VAULT</div>', unsafe_allow_html=True)
        st.markdown(f'<h1 class="main-title">Analysis: <span>{inputs["name"]}</span></h1>', unsafe_allow_html=True)
        st.write(f"Comprehensive analysis for {inputs['name']}, Age {inputs['age']} with {inputs['attendance']}% attendance.")
    
    # 1. Career Recommendation
    st.markdown('---')
    from src.career_recommendation.recommend import render_recommendations
    predicted_career = render_recommendations(**{k: v for k, v in inputs.items() if k not in ['name', 'age', 'attendance']})
    
    # Text-to-Speech Analysis Voice Driver
    components.html(f"""
        <script>
            function speakAnalysis() {{
                const synth = window.speechSynthesis;
                let voices = synth.getVoices();
                
                const playVoice = () => {{
                    voices = synth.getVoices();
                    // Prefer premium English female voices (Professional lady voice)
                    let voice = voices.find(v => (v.name.includes('Female') || v.name.includes('Zira') || v.name.includes('Samantha') || v.name.includes('Karen') || v.name.includes('Victoria') || v.name.includes('Google UK English Female') || v.name.includes('Google US English Female') || v.name.includes('Microsoft Zira') || v.name.includes('Moira') || v.name.includes('Tessa') || v.name.includes('Veena')) && v.lang.startsWith('en'));
                    if (!voice) voice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Female') || v.name.includes('Zira'))); // Secondary fallback
                    if (!voice) voice = voices.find(v => v.lang.startsWith('en')); // Ultimate fallback English
                    
                    const msg = new SpeechSynthesisUtterance("Hey {inputs['name']}. Analysis complete. Based on your cognitive mapping and artificial intelligence modeling, your ideal career pathway is {predicted_career}. Please review your DMIT profile and success roadmap.");
                    if(voice) msg.voice = voice;
                    msg.rate = 0.95;
                    msg.pitch = 1.05;
                    msg.volume = 1;
                    synth.speak(msg);
                }};

                if (voices.length === 0) {{
                    synth.onvoiceschanged = playVoice;
                }} else {{
                    playVoice();
                }}
            }}
            speakAnalysis();
        </script>
    """, height=0)
    
    # 2. DMIT Dashboard
    st.markdown('---')
    from src.dmit_dashboard.dashboard import render_dmit_dashboard
    render_dmit_dashboard(inputs['logical'], inputs['creative'], inputs['practical'])
    
    # 3. Career Roadmap
    st.markdown('---')
    from src.roadmap_generator.generator import render_roadmap
    render_roadmap(predicted_career)
    
    # 4. Skill Intelligence
    st.markdown('---')
    from src.skill_intelligence.intelligence import main as skill_main
    st.markdown('<h2 class="main-title">Skill <span>Intelligence</span></h2>', unsafe_allow_html=True)
    skill_main()

    st.markdown('---')
    
    # 5. Real PDF Generation Function
    from fpdf import FPDF
    def create_pdf(inputs, career):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 24)
        pdf.set_text_color(37, 99, 235)
        pdf.cell(200, 20, "LIFE VAULT ANALYSIS REPORT", ln=True, align='C')
        pdf.ln(10)
        
        pdf.set_font("Arial", 'B', 16)
        pdf.set_text_color(15, 23, 42)
        pdf.cell(200, 10, f"Analysis for {inputs['name']}", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.cell(200, 10, f"Age: {inputs['age']} | Attendance: {inputs['attendance']}%", ln=True)
        pdf.ln(5)
        
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, f"Recommended Career: {career}", ln=True)
        pdf.ln(10)
        
        pdf.set_font("Arial", 'B', 14)
        pdf.set_text_color(37, 99, 235)
        pdf.cell(200, 10, "Cognitive Score Summary:", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.set_text_color(15, 23, 42)
        for k, v in inputs.items():
            if k not in ['name', 'age', 'attendance']:
                pdf.cell(200, 8, f"- {str(k).capitalize()}: {v}%", ln=True)
        
        pdf.ln(20)
        pdf.set_font("Arial", 'I', 10)
        pdf.cell(200, 10, "Protected by Life Vault Secure Career Intelligence", align='C')
        return bytes(pdf.output())

    colP1, colP2 = st.columns([2, 1])
    with colP1:
        pdf_data = create_pdf(inputs, predicted_career)
        st.download_button(
            label="Download Complete Analysis (PDF)",
            data=pdf_data,
            file_name=f"LifeVault_Analysis_{inputs['name']}.pdf",
            mime="application/pdf",
            type="primary",
            use_container_width=True
        )
    with colP2:
        if st.button("Start New Assessment", type="secondary", use_container_width=True):
            st.session_state.report_generated = False
            st.rerun()

# 5. Permanent AI Counsellor at the bottom
st.markdown('---')
from src.counsellor_chatbot.chatbot import main as chatbot_main
st.markdown('<h2 class="main-title">AI <span>Counsellor</span></h2>', unsafe_allow_html=True)
chatbot_main()