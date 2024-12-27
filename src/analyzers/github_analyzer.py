"""
GitHub Repository Analyzer
"""
import os
from github import Github

class GitHubAnalyzer:
    def __init__(self, token=None):
        if token is None:
            token = os.getenv('GITHUB_TOKEN')
        self.github = Github(token)
        
    def analyze_repository(self, repo_name):
        try:
            repo = self.github.get_repo(repo_name)
            return {
                "name": repo.name,
                "description": repo.description,
                "stars": repo.stargazers_count,
                "language": repo.language,
                "topics": repo.get_topics()
            }
        except Exception as e:
            return {"error": str(e)}