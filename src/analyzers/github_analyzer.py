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
                "language": repo.language,
                "stars": repo.stargazers_count,
                "forks": repo.forks_count,
                "topics": repo.get_topics()
            }
        except Exception as e:
            return {"error": str(e)}
            
    def search_repositories(self, query, limit=10):
        try:
            repos = self.github.search_repositories(query=query)
            results = []
            for repo in repos[:limit]:
                results.append(self.analyze_repository(repo.full_name))
            return results
        except Exception as e:
            return {"error": str(e)}