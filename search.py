# search.py - Search functionality for TDS Virtual TA

from data import DISCOURSE_DATA, COURSE_CONTENT

def search_knowledge_base(question):
    """
    Search through discourse data and course content for relevant answers
    """
    question_lower = question.lower()
    
    # Direct keyword matching with discourse posts
    for post in DISCOURSE_DATA:
        # Check if any post keyword matches the question
        for keyword in post['keywords']:
            if keyword in question_lower:
                return {
                    "answer": post['content'],
                    "links": [
                        {
                            "url": post['url'],
                            "text": post['title']
                        }
                    ]
                }
    
    # Fallback to course content for general questions
    if any(word in question_lower for word in ['course', 'tds', 'modules', 'evaluation', 'tools', 'data science']):
        return {
            "answer": COURSE_CONTENT['content'],
            "links": [
                {
                    "url": COURSE_CONTENT['url'],
                    "text": "TDS Course Content"
                }
            ]
        }
    
    # Default response
    return {
        "answer": "I couldn't find a specific answer to your question. Please check the TDS Discourse forum or course materials for more detailed help.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34",
                "text": "TDS Knowledge Base"
            }
        ]
    }
