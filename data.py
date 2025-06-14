# data.py - Real discourse data from TDS course

# Real discourse data extracted from your provided content
DISCOURSE_DATA = [
    {
        'title': 'GA5 Question 8 Clarification',
        'content': 'Use the model mentioned in the question. For GPT questions, use gpt-3.5-turbo-0125 even if AI Proxy supports gpt-4o-mini. Use OpenAI API directly for this question.',
        'url': 'https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4',
        'keywords': ['gpt', 'model', 'openai', 'ai proxy', 'gpt-3.5-turbo'],
        'category': 'Graded Assignments'
    },
    {
        'title': 'Project1 - Virtual TA - Discussion Thread [TDS May 2025]',
        'content': 'Discussion thread for Project 1 Virtual TA. Use markdown code formatting when sharing code. Focus on API endpoint and GitHub repo requirements with MIT license.',
        'url': 'https://discourse.onlinedegree.iitm.ac.in/t/project1-virtual-ta-discussion',
        'keywords': ['project1', 'virtual ta', 'api', 'github', 'deployment', 'license'],
        'category': 'Projects'
    },
    {
        'title': 'CORS settings for the deployed project',
        'content': 'Configure CORS in FastAPI using: from fastapi.middleware.cors import CORSMiddleware. Add allow_origins=["*"] for development, specific origins for production.',
        'url': 'https://discourse.onlinedegree.iitm.ac.in/t/cors-settings-deployed-project',
        'keywords': ['cors', 'fastapi', 'deployment', 'middleware', 'headers'],
        'category': 'Technical Issues'
    },
    {
        'title': 'Help required in Project 1 - scrapping Discourse data',
        'content': 'Students need help with scraping Discourse data for Virtual TA project. Authentication issues are common. Alternative: manually collect key discussions and create knowledge base.',
        'url': 'https://discourse.onlinedegree.iitm.ac.in/t/help-scraping-discourse-data',
        'keywords': ['scraping', 'discourse', 'authentication', 'api', 'data collection'],
        'category': 'Technical Issues'
    },
    {
        'title': 'Npx -y promptfoo eval –config project-tds-virtual-ta-promptfoo.yaml error',
        'content': 'Issues running evaluation script for Virtual TA project. Check API endpoint URL in config file and ensure your deployed API is accessible.',
        'url': 'https://discourse.onlinedegree.iitm.ac.in/t/promptfoo-eval-error',
        'keywords': ['promptfoo', 'evaluation', 'yaml', 'config', 'error', 'api endpoint'],
        'category': 'Evaluation'
    }
]

# Course content from TDS materials
COURSE_CONTENT = {
    'content': '''Tools in Data Science (TDS) is a practical diploma-level course at IIT Madras covering 7 modules:
1. Development Tools - Git, Python, IDEs
2. Deployment Tools - Docker, Cloud platforms, CI/CD  
3. Large Language Models - OpenAI, Claude, local LLMs
4. Data Sourcing - Web scraping, APIs, databases
5. Data Preparation - Cleaning, transformation, validation
6. Data Analysis - Statistics, machine learning, insights
7. Data Visualization - Charts, dashboards, storytelling

Evaluation: GA (15%), Project 1 (20%), ROE (20%), Project 2 (20%), Final (25%)''',
    'url': 'https://tds.s-anand.net/#/2025-01/'
}
