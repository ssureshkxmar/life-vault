import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
import uvicorn
import datetime

# Cloudflare Configuration
CLOUDFLARE_ACCOUNT_ID = "beb7787ed2562d195ccdd4d66f8c4e70"
CLOUDFLARE_API_TOKEN = "cfat_OOu4fRUw9fJRat5Eji88fBFVzmJH95QStNIrgoMI52efb3d0"
MODEL_ID = "@cf/meta/llama-3-8b-instruct"

app = FastAPI(
    title="Life Vault | Career Intelligence Platform",
    description="Professional Student Career & Guidance API",
    version="2.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-Memory Storage (Mock DB)
attendance_logs: List[Dict[str, str]] = []

# Data Models
class StudentProfile(BaseModel):
    name: str
    age: int
    aptitude_score: float
    interest_score: float
    dmit_traits: dict
    academic_background: float

class ChatInput(BaseModel):
    user_message: str
    history: Optional[List[Dict[str, str]]] = []

class AttendanceEntry(BaseModel):
    name: str
    student_id: str
    course: str
    section: str
    date: str
    status: str
    remarks: Optional[str] = ""

# --- Professional AI Chat Implementation ---
@app.post("/api/chat")
async def professional_chat(chat_in: ChatInput):
    """Process user query through advanced Cloudflare Workers AI"""
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/{MODEL_ID}"
    headers = {"Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}"}
    
    system_prompt = {
        "role": "system",
        "content": "You are Life Vault AI, a professional career counsellor. Provide extremely detailed, step-by-step career path analysis. Suggest certifications, tech stacks, and soft skills needed for any profession mentioned. Help students navigate school and college choices with expert-level detail."
    }
    
    messages = [system_prompt]
    if chat_in.history:
        messages.extend(chat_in.history)
    messages.append({"role": "user", "content": chat_in.user_message})

    try:
        response = requests.post(url, headers=headers, json={"messages": messages}, timeout=60)
        if response.status_code == 200:
            result = response.json()
            return {"response": result["result"]["response"], "status": "success"}
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except Exception as e:
        return {"response": f"The Life Vault AI core is currently under maintenance. Please try again soon. Detail: {str(e)}", "status": "error"}

# --- Career & DMIT Implementation ---
@app.post("/api/recommend-career")
async def recommend_career(profile: StudentProfile):
    """Generate career recommendations based on student profile"""
    # Professional Logic (Simplified Mock)
    recs = [
        {"career": "Data Science", "score": 0.95, "reasoning": "High logical traits and math aptitude discovered in DMIT."},
        {"career": "AI Research", "score": 0.92, "reasoning": "Creative problem solving combined with academic excellence."},
        {"career": "Cybersecurity", "score": 0.88, "reasoning": "Strong analytical foundation matching industry trends."}
    ]
    return {"student": profile.name, "recommendations": recs}

@app.get("/api/dmit/{student_id}")
async def get_dmit_data(student_id: str):
    return {
        "traits": {"logical": 85, "creative": 70, "practical": 60, "social": 75, "leadership": 80},
        "brain_dominance": {"left_brain": 75, "right_brain": 65}
    }

@app.get("/api/roadmap/{career}")
async def get_roadmap(career: str):
    return {
        "career": career,
        "roadmap": [
            {"stage": "Skill Foundation (Year 1)", "duration": "1 year", "description": "Master core languages and logic.", "skills": ["Python", "Algorithms"]},
            {"stage": "Specialization (Year 2)", "duration": "1 year", "description": "Deep dive into career-specific frameworks.", "skills": ["Machine Learning", "FastAPI"]}
        ]
    }

# --- Attendance Implementation ---
@app.post("/api/attendance")
async def log_attendance(entry: AttendanceEntry):
    attendance_logs.append(entry.dict())
    return {"message": "Attendance logged successfully", "data": entry}

@app.get("/api/attendance")
async def get_attendance_history():
    return {"history": attendance_logs[-10:]} # Return last 10 logs

@app.get("/api/school-analytics/{school_id}")
async def school_analytics(school_id: str):
    return {
        "class_wise_metrics": {
            "Class 8": {"avg_aptitude": 70, "students": 45},
            "Class 9": {"avg_aptitude": 75, "students": 48}
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)