"""
AI Project Planner using Gemini
"""
import os
import google.generativeai as genai

class AIProjectPlanner:
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
    def analyze_project(self, project_idea):
        prompt = f"""
        Analyze this project idea and provide detailed recommendations:
        {project_idea}
        
        Please provide:
        1. Technical requirements
        2. Suggested architecture
        3. Technology stack
        4. Implementation steps
        5. Potential challenges
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return {"error": str(e)}
            
    def suggest_resources(self, project_analysis):
        prompt = f"""
        Based on this project analysis, suggest learning resources and tools:
        {project_analysis}
        
        Please provide:
        1. Tutorials and documentation
        2. GitHub repositories
        3. Development tools
        4. Learning resources
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return {"error": str(e)}