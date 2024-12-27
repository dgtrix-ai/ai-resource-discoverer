# AI Resource Discoverer

An AI-powered development resource analyzer and project planner that helps developers discover and organize resources for their projects.

## Features

1. Project Analysis
   - Technical requirements analysis
   - Architecture recommendations
   - Technology stack suggestions
   - Implementation planning

2. Resource Discovery
   - GitHub repository analysis
   - Learning resource suggestions
   - Development tool recommendations
   - Best practices guidelines

3. AI Integration
   - Google Gemini AI for project analysis
   - GitHub API for repository discovery
   - Smart resource matching

## Setup

1. Clone the repository
2. Create a `.env` file with your API keys:
   ```
   GITHUB_TOKEN=your_github_token
   GEMINI_API_KEY=your_gemini_api_key
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```python
from src.analyzers.github_analyzer import GitHubAnalyzer
from src.planners.ai_project_planner import AIProjectPlanner

# Initialize components
analyzer = GitHubAnalyzer()
planner = AIProjectPlanner()

# Analyze a project idea
project_analysis = planner.analyze_project("Create a web-based task management system")

# Find relevant resources
repositories = analyzer.search_repositories("task management system")