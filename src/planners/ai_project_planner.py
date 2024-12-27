"""
AI Project Planner using Gemini
"""
import google.generativeai as genai

class AIProjectPlanner:
    def __init__(self, api_key="AIzaSyATqrCOp_VZWQXFcbzppCUcRcPE2r90crw"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
    def analyze_project(self, project_idea):
        try:
            response = self.model.generate_content(
                f"Analyze this project idea and provide technical recommendations: {project_idea}"
            )
            return response.text
        except Exception as e:
            return {"error": str(e)}