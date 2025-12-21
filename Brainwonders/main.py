from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Brainwonders AI Platform API",
    description="Career Intelligence & Counselling Platform",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class StudentProfile(BaseModel):
    name: str
    age: int
    aptitude_score: float
    interest_score: float
    dmit_traits: dict
    academic_background: float

class CareerRecommendation(BaseModel):
    career: str
    suitability_score: float
    reasoning: str

class RoadmapStep(BaseModel):
    stage: str
    duration: str
    description: str
    skills: List[str]

# Routes
@app.get("/")
async def root():
    return {
        "message": "Welcome to Brainwonders AI Platform",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Career Recommendation Endpoints
@app.post("/api/recommend-career")
async def recommend_career(profile: StudentProfile):
    """Generate career recommendations based on student profile"""
    return {
        "student": profile.name,
        "recommendations": [
            {
                "career": "Data Science",
                "score": 0.95,
                "reasoning": "Your logical thinking and high aptitude match this field"
            }
        ]
    }

@app.get("/api/careers")
async def list_careers():
    """Get list of available careers"""
    return {
        "careers": [
            "Data Science", "Medicine", "Engineering", "Arts",
            "Commerce", "Trades", "Design", "Law"
        ]
    }

# DMIT Dashboard Endpoints
@app.get("/api/dmit/{student_id}")
async def get_dmit_data(student_id: str):
    """Get DMIT analysis for a student"""
    return {
        "student_id": student_id,
        "traits": {
            "logical": 85,
            "creative": 70,
            "practical": 60,
            "social": 75,
            "leadership": 80
        },
        "brain_dominance": {
            "left_brain": 75,
            "right_brain": 65
        }
    }

# Roadmap Endpoints
@app.get("/api/roadmap/{career}")
async def get_roadmap(career: str):
    """Generate career roadmap for a specific career"""
    return {
        "career": career,
        "roadmap": [
            {
                "stage": "Class 8-10",
                "duration": "3 years",
                "description": "Build foundational math and science skills",
                "skills": ["Mathematics", "Physics", "Chemistry"]
            },
            {
                "stage": "Class 11-12",
                "duration": "2 years",
                "description": "Specialize in PCM or chosen stream",
                "skills": ["Advanced Math", "Programming Basics"]
            }
        ]
    }

# Chatbot Endpoints
@app.post("/api/chat")
async def chat(user_message: str):
    """Process user query through AI counsellor"""
    return {
        "response": "Thank you for your question. Based on your profile, I recommend exploring Data Science.",
        "confidence": 0.85
    }

# Skill Intelligence Endpoints
@app.get("/api/school-analytics/{school_id}")
async def school_analytics(school_id: str):
    """Get school-wide skill analytics"""
    return {
        "school_id": school_id,
        "class_wise_metrics": {
            "class_8": {"avg_aptitude": 70, "students": 45},
            "class_9": {"avg_aptitude": 75, "students": 48}
        }
    }

@app.get("/api/corporate-analytics/{company_id}")
async def corporate_analytics(company_id: str):
    """Get corporate skill gap analysis"""
    return {
        "company_id": company_id,
        "skill_gaps": {
            "python": 20,
            "machine_learning": 30,
            "communication": 15
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)