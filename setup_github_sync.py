#!/usr/bin/env python3
from github import Github
import os
import subprocess

class GitHubSyncManager:
    def __init__(self, token):
        self.token = token
        self.g = Github(token)
        self.repo_name = "ai-resource-discoverer"
        self.repo = None
        
    def setup_repository(self):
        try:
            # Create or get repository
            user = self.g.get_user()
            try:
                self.repo = user.get_repo(self.repo_name)
                print(f"Repository {self.repo_name} already exists")
            except:
                self.repo = user.create_repo(
                    self.repo_name,
                    description="AI-powered development resource analyzer and project planner",
                    private=False
                )
                print(f"Created new repository: {self.repo_name}")
            return True
        except Exception as e:
            print(f"Error setting up repository: {str(e)}")
            return False

    def setup_local_git(self):
        try:
            # Initialize git if needed
            if not os.path.exists('.git'):
                subprocess.run(['git', 'init'])
            
            # Configure git
            subprocess.run(['git', 'config', 'user.name', 'AI Resource Discoverer'])
            subprocess.run(['git', 'config', 'user.email', 'ai.resource.discoverer@example.com'])
            
            # Add remote
            remote_url = f"https://{self.token}@github.com/{self.g.get_user().login}/{self.repo_name}.git"
            subprocess.run(['git', 'remote', 'remove', 'origin'], stderr=subprocess.PIPE)
            subprocess.run(['git', 'remote', 'add', 'origin', remote_url])
            return True
        except Exception as e:
            print(f"Error setting up local git: {str(e)}")
            return False

    def sync_files(self):
        try:
            # Add all files
            subprocess.run(['git', 'add', '.'])
            
            # Commit
            subprocess.run(['git', 'commit', '-m', 'Initial commit: Project setup and sync'])
            
            # Push to main branch
            subprocess.run(['git', 'push', '-u', 'origin', 'main'])
            return True
        except Exception as e:
            print(f"Error syncing files: {str(e)}")
            return False

def main():
    token = os.getenv('GITHUB_TOKEN')
    sync_manager = GitHubSyncManager(token)
    
    print("Setting up GitHub repository...")
    if sync_manager.setup_repository():
        print("GitHub repository setup complete")
        
        print("Setting up local git...")
        if sync_manager.setup_local_git():
            print("Local git setup complete")
            
            print("Syncing files...")
            if sync_manager.sync_files():
                print("Files synced successfully")
            else:
                print("Failed to sync files")
        else:
            print("Failed to setup local git")
    else:
        print("Failed to setup GitHub repository")

if __name__ == "__main__":
    main()