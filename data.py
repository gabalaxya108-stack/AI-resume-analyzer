"""
data.py

Centralized Data Layer for the AI Resume Analyzer.
This file stores the global taxonomy of predefined skills, target job benchmarks,
and the curated educational pathways mapping directly to technical gaps.
"""

# Categorical skills recognized by the AI Analyzer
PREDEFINED_SKILLS = {
    "agile", "api design", "aws", "bash", "big data", "c#", "c++", "cloud computing", 
    "communication", "css", "data analysis", "data visualization", "deep learning", 
    "django", "docker", "excel", "fastapi", "figma", "flask", "git", "go", "html", 
    "java", "javascript", "jira", "kubernetes", "leadership", "linux", 
    "machine learning", "mongodb", "mysql", "nlp", "node", "node.js", "nosql", 
    "numpy", "pandas", "postgresql", "powerbi", "problem solving", 
    "product management", "python", "pytorch", "react", "ruby", "rust", 
    "scikit-learn", "scrum", "spring boot", "sql", "statistics", "tableau", 
    "tensorflow", "ui/ux", "vue"
}

# Priority-based Mapping Matrix
JOB_ROLES = {
    "Software Developer": {
        "high_priority": ["python", "java", "javascript", "git"],
        "medium_priority": ["sql", "api design", "docker", "agile", "node.js"],
        "low_priority": ["aws", "kubernetes", "react", "c++", "c#", "linux", "mongodb"]
    },
    "Data Scientist": {
        "high_priority": ["python", "machine learning", "sql", "pandas", "numpy"],
        "medium_priority": ["scikit-learn", "data visualization", "statistics", "tableau"],
        "low_priority": ["tensorflow", "pytorch", "deep learning", "docker", "aws", "nlp", "big data"]
    },
    "Data Analyst": {
        "high_priority": ["sql", "excel", "data analysis", "tableau"],
        "medium_priority": ["python", "pandas", "powerbi", "communication"],
        "low_priority": ["statistics", "machine learning", "aws", "problem solving"]
    },
    "Product Manager": {
        "high_priority": ["product management", "agile", "communication", "leadership"],
        "medium_priority": ["jira", "scrum", "data analysis", "problem solving"],
        "low_priority": ["ui/ux", "sql", "figma", "cloud computing"]
    },
    "UI/UX Designer": {
        "high_priority": ["ui/ux", "figma", "html", "css", "communication"],
        "medium_priority": ["javascript", "agile", "data visualization"],
        "low_priority": ["react", "vue", "problem solving", "product management"]
    }
}

# Targeted Learning Course Recommendations
SKILL_RESOURCES = {
    "python": {
        "youtube_title": "Python Tutorial for Beginners - Programming with Mosh",
        "youtube_link": "https://www.youtube.com/watch?v=_uQrJ0TkZlc",
        "course_title": "100 Days of Code: The Complete Python Pro Bootcamp (Udemy)",
        "course_link": "https://www.udemy.com/course/100-days-of-code/"
    },
    "java": {
        "youtube_title": "Java Programming All-in-One - freeCodeCamp",
        "youtube_link": "https://www.youtube.com/watch?v=A74TOX803D0",
        "course_title": "Java Programming and Software Engineering Fundamentals (Coursera)",
        "course_link": "https://www.coursera.org/specializations/java-programming"
    },
    "sql": {
        "youtube_title": "SQL Full Course | Database Management - freeCodeCamp",
        "youtube_link": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
        "course_title": "The Ultimate MySQL Bootcamp: Go from SQL Beginner to Expert (Udemy)",
        "course_link": "https://www.udemy.com/course/the-ultimate-mysql-bootcamp-go-from-sql-beginner-to-expert/"
    },
    "javascript": {
        "youtube_title": "JavaScript Crash Course - Traversy Media",
        "youtube_link": "https://www.youtube.com/watch?v=hdI2bqOjy3c",
        "course_title": "The Complete JavaScript Course: From Zero to Expert! (Udemy)",
        "course_link": "https://www.udemy.com/course/the-complete-javascript-course/"
    },
    "react": {
        "youtube_title": "React JS Full Course - freeCodeCamp",
        "youtube_link": "https://www.youtube.com/watch?v=bMknfKXIFA8",
        "course_title": "Meta Front-End Developer Professional Certificate (Coursera)",
        "course_link": "https://www.coursera.org/professional-certificates/meta-front-end-developer"
    },
    "node.js": {
        "youtube_title": "Node.js and Express.js - freeCodeCamp",
        "youtube_link": "https://www.youtube.com/watch?v=Oe421EPjeBE",
        "course_title": "NodeJS - The Complete Guide (REST APIs, GraphQL) (Udemy)",
        "course_link": "https://www.udemy.com/course/nodejs-the-complete-guide/"
    },
    "aws": {
        "youtube_title": "AWS Certified Cloud Practitioner - freeCodeCamp",
        "youtube_link": "https://www.youtube.com/watch?v=SOTamWNgDKc",
        "course_title": "Ultimate AWS Certified Solutions Architect Associate (Udemy)",
        "course_link": "https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/"
    },
    "docker": {
        "youtube_title": "Docker Tutorial for Beginners - TechWorld with Nana",
        "youtube_link": "https://www.youtube.com/watch?v=3c-iBn73dDE",
        "course_title": "Docker Mastery: with Kubernetes +Swarm (Udemy)",
        "course_link": "https://www.udemy.com/course/docker-mastery/"
    },
    "kubernetes": {
        "youtube_title": "Kubernetes Tutorial for Beginners - TechWorld with Nana",
        "youtube_link": "https://www.youtube.com/watch?v=X48VuDVv0do",
        "course_title": "Kubernetes for the Absolute Beginners (Udemy)",
        "course_link": "https://www.udemy.com/course/learn-kubernetes/"
    },
    "machine learning": {
        "youtube_title": "Machine Learning Crash Course - Google",
        "youtube_link": "https://www.youtube.com/watch?v=cKxRvEZd3Mw",
        "course_title": "Machine Learning Specialization by Andrew Ng (Coursera)",
        "course_link": "https://www.coursera.org/specializations/machine-learning-introduction"
    },
    "pandas": {
        "youtube_title": "Data Analysis with Python - freeCodeCamp",
        "youtube_link": "https://www.youtube.com/watch?v=r-uOLxNrNk8",
        "course_title": "Data Analysis with Pandas and Python (Udemy)",
        "course_link": "https://www.udemy.com/course/data-analysis-with-pandas/"
    },
    "agile": {
        "youtube_title": "Agile Scrum Master Training - Simplilearn",
        "youtube_link": "https://www.youtube.com/watch?v=9TycLR0TqFA",
        "course_title": "Google Project Management Certificate (Coursera)",
        "course_link": "https://www.coursera.org/professional-certificates/google-project-management"
    },
    "git": {
        "youtube_title": "Git and GitHub for Beginners - freeCodeCamp",
        "youtube_link": "https://www.youtube.com/watch?v=RGOj5yH7evk",
        "course_title": "Version Control with Git (Coursera)",
        "course_link": "https://www.coursera.org/learn/version-control-with-git"
    },
    "ui/ux": {
        "youtube_title": "UI/UX Design Tutorial For Beginners - Envato Tuts+",
        "youtube_link": "https://www.youtube.com/watch?v=c9Wg6Cb_YlU",
        "course_title": "Google UX Design Professional Certificate (Coursera)",
        "course_link": "https://www.coursera.org/professional-certificates/google-ux-design"
    },
    "tableau": {
        "youtube_title": "Tableau Full Course - Edureka",
        "youtube_link": "https://www.youtube.com/watch?v=aHaOIvR00So",
        "course_title": "Data Visualization with Tableau Specialization (Coursera)",
        "course_link": "https://www.coursera.org/specializations/data-visualization"
    }
}
