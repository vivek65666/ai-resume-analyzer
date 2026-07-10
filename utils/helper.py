import os
import json
import requests
from utils.prompts import RESUME_ANALYSIS_PROMPT

def analyze_resume_with_llm(resume_text: str, job_description: str, model: str = "gemini-2.5-flash") -> dict:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"ats_score": 0, "skills_match": [], "missing_skills": [], "structural_improvements": ["Missing GEMINI_API_KEY inside environment store."], "verdict": "Config Error"}
        
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    formatted_prompt = RESUME_ANALYSIS_PROMPT.format(
        job_description=job_description,
        resume_text=resume_text
    )
    
    payload = {
        "contents": [
            {
                "parts": [{"text": formatted_prompt}]
            }
        ],
        "generationConfig": {
            "responseMimeType": "application/json",
            "temperature": 0.2
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response_data = response.json()
        
        # Check if the API returned an explicit error block
        if "error" in response_data:
            return {
                "ats_score": 0, "skills_match": [], "missing_skills": [],
                "structural_improvements": [f"Gemini API Error: {response_data['error'].get('message', 'Unknown API Error')}"],
                "verdict": "API Error"
            }
        
        # Pull text safely out of Google's response object nesting layers
        response_text = response_data['candidates'][0]['content']['parts'][0]['text']
        
        return json.loads(response_text)
        
    except Exception as e:
        return {
            "ats_score": 0,
            "skills_match": [],
            "missing_skills": [],
            "structural_improvements": [f"REST execution pipeline error: {str(e)}", f"Raw Response Data: {str(response_data) if 'response_data' in locals() else 'None'}"],
            "verdict": "Error processing document"
        }