"""
backend.py

Core Intelligence Logic Layer for the AI Resume Analyzer.
Exposes modular Object-Oriented Engine classes to process Skill Gap Intelligence algorithms, map Course Recommendations,
and strictly parse Generative LLM logic structures securely.
"""

import pdfplumber
import re
from typing import List, Dict, Any, Optional
from data import SKILL_RESOURCES

class ResumeProcessor:
    """
    Handles PDF ingestion and textual extraction securely, ensuring no internal 
    text strings are exposed unsafely via data hiding.
    """
    def __init__(self):
        self.__text = ""
        self.__skills_found: List[str] = []

    def ingest_pdf(self, file) -> None:
        """Safely iterates through an uploaded PDF file and extracts all readable text."""
        self.__text = ""
        try:
            with pdfplumber.open(file) as pdf:
                if not pdf.pages:
                    raise ValueError("The uploaded PDF file contains zero pages.")
                    
                for page in pdf.pages:
                    extracted = page.extract_text()
                    if extracted:
                        self.__text += extracted + "\n"
                        
            cleaned_text = self.__text.strip()
            if not cleaned_text:
                raise ValueError("No readable text found. Please ensure this is not an image-based scan.")
                
            self.__text = cleaned_text
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise Exception(f"Corrupted file structure encountered. Internals: {str(e)}")

    def extract_skills(self, skill_list: List[str]) -> None:
        """Identifies predefined taxonomy elements dynamically mapped across aliases."""
        if not self.__text:
            return

        text_lower = self.__text.lower()
        found_skills = set()
        alias_map = {
            "react.js": "react", "reactjs": "react",
            "node.js": "node", "nodejs": "node",
            "vue.js": "vue", "vuejs": "vue",
            "golang": "go"
        }
        
        for skill in skill_list:
            skill_lower = skill.lower()
            try:
                pattern = rf'\b{re.escape(skill_lower)}\b' if skill_lower not in ["c++", "c#"] else rf'c\{skill_lower[1:]}'
                if re.search(pattern, text_lower):
                    found_skills.add(skill)
                    continue
                    
                for alias, standard in alias_map.items():
                    if standard == skill_lower:
                        alias_pattern = rf'\b{re.escape(alias)}\b'
                        if re.search(alias_pattern, text_lower):
                            found_skills.add(skill)
                            break
            except Exception:
                continue
                
        self.__skills_found = list(found_skills)

    @property
    def raw_text(self) -> str:
        """Read-only access to extracted text."""
        return self.__text
        
    @property
    def skills_found(self) -> List[str]:
        """Read-only access to found skills."""
        return self.__skills_found


class CareerLogicEngine:
    """
    Skill Gap Intelligence Engine:
    Calculates weighted grading mapping to explicit Strong, Weak, and Missing paradigms using OOP structure.
    """
    
    def __init__(self, raw_text: str, skills_found: List[str], role_requirements: Dict[str, List[str]], target_role: str):
        self.__raw_text = raw_text
        self.__skills_found = skills_found
        self.__role_requirements = role_requirements
        self.__target_role = target_role
        
        self.__intel: Dict[str, Any] = {}
        self.__suggestions: List[str] = []
        self.__roadmap: Dict[str, List[str]] = {}
        self.__resources: Dict[str, Dict[str, str]] = {}
        
    def evaluate(self) -> None:
        """Run all algorithmic internal routines consecutively."""
        self.__evaluate_skill_gaps()
        self.__generate_suggestions()
        self.__generate_roadmap()
        self.__get_resources()

    def __evaluate_skill_gaps(self) -> None:
        """Internal skill gap calculation logic."""
        try:
            text_lower = self.__raw_text.lower()
            found_set = {s.lower() for s in self.__skills_found} if self.__skills_found else set()
            
            req_high = {s.lower(): s for s in self.__role_requirements.get("high_priority", [])}
            req_med = {s.lower(): s for s in self.__role_requirements.get("medium_priority", [])}
            req_low = {s.lower(): s for s in self.__role_requirements.get("low_priority", [])}
            
            strong_skills = []
            weak_skills = []
            missing_high = []
            missing_med = []
            missing_low = []
            
            earned_pts = 0
            max_pts = 0
            
            for lower_req, original in req_high.items():
                max_pts += 5
                if lower_req in found_set:
                    earned_pts += 5
                    strong_skills.append(original)
                else:
                    missing_high.append(original)
                    
            for lower_req, original in req_med.items():
                max_pts += 3
                if lower_req in found_set:
                    earned_pts += 3
                    strong_skills.append(original)
                else:
                    missing_med.append(original)
                    
            for lower_req, original in req_low.items():
                max_pts += 1
                if lower_req in found_set:
                    earned_pts += 1
                    weak_skills.append(original)
                else:
                    missing_low.append(original)
                    
            target_all_lower = set(req_high.keys()).union(set(req_med.keys())).union(set(req_low.keys()))
            for s in self.__skills_found:
                if s.lower() not in target_all_lower:
                    if s not in weak_skills:
                        weak_skills.append(s)

            impact_keywords = {
                 "project", "experience", "led", "managed", "developed", 
                 "achieved", "improved", "increased", "designed", "optimized",
                 "reduced", "spearheaded", "team", "deployed", "architected"
            }
            impact_matches = sum(1 for kw in impact_keywords if re.search(rf'\b{kw}\b', text_lower))
            max_pts += 15
            earned_pts += min(impact_matches * 3, 15)
            
            max_pts += 10
            word_count = len(text_lower.split())
            if 300 <= word_count <= 850:
                earned_pts += 10
            elif 150 <= word_count < 300 or 850 < word_count <= 1100:
                earned_pts += 5
            else:
                earned_pts += 2
                
            score = int((earned_pts / max_pts) * 100) if max_pts > 0 else 0
            score = min(score, 100)
            
            if score < 40:
                level = "Beginner"
            elif 40 <= score <= 75:
                level = "Intermediate"
            else:
                level = "Job Ready"
                
            self.__intel = {
                "score": score,
                "level": level,
                "strong_skills": strong_skills,
                "weak_skills": weak_skills,
                "missing_high": missing_high,
                "missing_med": missing_med,
                "missing_low": missing_low
            }
        except Exception:
            self.__intel = {
                "score": 0, "level": "Beginner",
                "strong_skills": [], "weak_skills": [],
                "missing_high": [], "missing_med": [], "missing_low": []
            }

    def __generate_suggestions(self) -> None:
        """Outputs dynamic algorithmic feedback recommendations."""
        suggestions = []
        
        missing_critical = self.__intel.get("missing_high", [])
        missing_medium = self.__intel.get("missing_med", [])
        level = self.__intel.get("level", "Beginner")
        
        if not missing_critical and not missing_medium:
            suggestions.append("🌟 Incredible alignment! You possess nearly all relevant benchmark skills expected.")
        elif missing_critical:
            suggestions.append(f"🚨 Critical Failure: You lack HIGH priority skills required for this job: {', '.join(missing_critical[:3]).title()}.")
        elif missing_medium:
            suggestions.append(f"⚠️ Medium Gap Detected: Consider acquiring tangible experiences incorporating: {', '.join(missing_medium[:3]).title()}.")

        if level == "Job Ready":
            suggestions.append("🚀 Job Ready Profile: Ensure your accomplishments are backed by strictly measurable numbers (e.g. 30% reduction).")
        elif level == "Intermediate":
            suggestions.append("📈 Intermediate Assessment: Injecting impactful 'action verbs' and covering medium-priority skills will rapidly elevate your output.")
        else:
            suggestions.append("📉 Beginner Threshold: The engine natively could not parse enough critical target requirements or sufficient technical impact statements.")
            
        self.__suggestions = suggestions

    def __generate_roadmap(self) -> None:
        """Generates a highly structured, hierarchical career path mirroring an explicit node-based graph."""
        missing_high = self.__intel.get("missing_high", [])
        missing_med = self.__intel.get("missing_med", [])
        missing_low = self.__intel.get("missing_low", [])
        weak_skills = self.__intel.get("weak_skills", [])
        level = self.__intel.get("level", "Beginner")
        
        # Structure will be { PhaseName: [ { "topic": "Name", "items": ["sub1", "sub2"] } ] }
        roadmap = {}
        
        # Helper to generate detailed granular topics for skills
        def get_details(skill):
            s = skill.lower()
            if "react" in s:
                return ["JSX & Components", "State & Props", "Hooks (useEffect, useState)", "Context API", "Routing & Suspense"]
            elif "python" in s:
                return ["Data Types & Structures", "Functions & OOP", "Decorators & Generators", "Asyncio", "Package Management"]
            elif "node" in s:
                return ["Event Loop", "Express.js Routing", "Middleware", "Database Connections", "Security (JWT, Passport)"]
            elif "sql" in s or "database" in s:
                return ["Relational Algebra", "Joins, Group By, Unions", "Indexing & Optimization", "Stored Procedures", "Normalization"]
            elif "java" in s:
                return ["JVM Architecture", "Classes, Interfaces, Enums", "Collections Framework", "Spring Boot Basics", "Concurrency"]
            elif "aws" in s or "cloud" in s:
                return ["IAM & Permissions", "Compute (EC2/Lambda)", "Storage (S3)", "VPC & Networking", "Deployment & CI/CD Pipelines"]
            else:
                return [f"Understand {skill} core architecture concepts", f"Set up local development for {skill}", f"Build a standardized CRUD implementation in {skill}", f"Deploy an atomic component utilizing {skill}"]

        if level == "Beginner":
            p1 = []
            for m in missing_high:
                p1.append({"topic": f"Master {m.title()} Fundamentals", "items": get_details(m)})
            if not p1: p1 = [{"topic": f"Core {self.__target_role} Architecture", "items": ["Understand ecosystem", "Configure development environment", "Learn foundational language syntax"]}]
            roadmap["Phase 1: First Principles & Syntactic Mastery"] = p1
            
            p2 = []
            for m in missing_med:
                p2.append({"topic": f"Expand into {m.title()}", "items": get_details(m)})
            for w in weak_skills:
                p2.append({"topic": f"Solidify {w.title()} Understanding", "items": get_details(w)})
            if not p2: p2 = [{"topic": "Secondary Tools Integration", "items": ["Learn standard CI/CD logic", "Configure testing frameworks"]}]
            roadmap["Phase 2: Capability Hardening"] = p2
            
            roadmap["Phase 3: Real World Applicability"] = [
                {"topic": "Capstone Architecture", "items": ["Design database schemas", "Build REST APIs", "Map Frontend interactions", "Automate deployment flow"]}
            ]
            
        elif level == "Intermediate":
            p1 = []
            for m in missing_high:
                p1.append({"topic": f"Bridge Core Vulnerability: {m.title()}", "items": get_details(m)})
            if not p1: p1 = [{"topic": "Advance Ecosystem Tools", "items": ["Master Docker containers", "Implement Redis caching"]}]
            roadmap["Phase 1: Eliminating Deficiencies"] = p1
            
            p2 = []
            for w in weak_skills:
                p2.append({"topic": f"Transforming {w.title()} to Strength", "items": get_details(w)})
            for m in missing_med + missing_low:
                p2.append({"topic": f"Satisfy Corporate ATS with {m.title()}", "items": get_details(m)})
            if not p2: p2 = [{"topic": "System Design Implementation", "items": ["Analyze monolithic vs microservices", "Implement robust logging algorithms"]}]
            roadmap["Phase 2: Architectural Optimization"] = p2
            
        else: # Job Ready
            p1 = []
            # Gather minor faults
            for m in missing_high + missing_med + weak_skills:
                 p1.append({"topic": f"Edge Optimization: {m.title()}", "items": [f"Review advanced interview questions for {m}", f"Refactor existing code utilizing modern {m} practices"]})
            if not p1: p1 = [{"topic": "Interview Penetration", "items": ["System Design Mock Interviews", "Algorithmic grinding (LeetCode/HackerRank)"]}]
            roadmap["Phase 1: Final Polish & Mock Scenarios"] = p1
            
            roadmap["Phase 2: Strategic Network Outreach"] = [
                {"topic": "Professional Positioning", "items": ["Quantify all resume bullet points", "Optimize LinkedIn keywords", "Contribute publicly to Open Source logic workflows", "Submit aggressive cold applications"]}
            ]
            
        self.__roadmap = roadmap

    def __get_resources(self) -> None:
        """Resource Recommendation Engine mappings."""
        resources = {}
        missing_all = self.__intel.get("missing_high", []) + self.__intel.get("missing_med", []) + self.__intel.get("missing_low", [])
        weak_skills = self.__intel.get("weak_skills", [])
        
        target_skills = list(set([s.lower() for s in missing_all + weak_skills]))
        
        for skill_lower in target_skills:
            if skill_lower in SKILL_RESOURCES:
                resources[skill_lower] = SKILL_RESOURCES[skill_lower]
            else:
                encoded_skill = skill_lower.replace(' ', '+')
                resources[skill_lower] = {
                    "youtube_title": f"{skill_lower.title()} Crash Course (YouTube)",
                    "youtube_link": f"https://www.youtube.com/results?search_query={encoded_skill}+crash+course",
                    "course_title": f"{skill_lower.title()} Fundamentals",
                    "course_link": f"https://www.google.com/search?q={encoded_skill}+course+udemy+coursera"
                }
                
        self.__resources = resources

    # Encapsulated Read-only Properties
    @property
    def target_role(self) -> str:
        return self.__target_role

    @property
    def intel(self) -> Dict[str, Any]:
        return self.__intel

    @property
    def suggestions(self) -> List[str]:
        return self.__suggestions

    @property
    def roadmap(self) -> Dict[str, List[str]]:
        return self.__roadmap

    @property
    def resources(self) -> Dict[str, Dict[str, str]]:
        return self.__resources

    @property
    def missing_all_skills(self) -> List[str]:
        return self.__intel.get("missing_high", []) + self.__intel.get("missing_med", []) + self.__intel.get("missing_low", [])

    @property
    def weak_skills(self) -> List[str]:
        return self.__intel.get("weak_skills", [])


class GenerativeAIEngine:
    """
    Handles all interactions with Google Gemini, deeply isolating API keys and authentication logic securely.
    """
    
    def __init__(self, api_key: str):
        self.__api_key = api_key
        self.__is_configured = False
        self.__configure_api()

    def __configure_api(self):
        """Privately configure the AI library."""
        try:
            import google.generativeai as genai
            if self.__api_key:
                genai.configure(api_key=self.__api_key)
                self.__model = genai.GenerativeModel('gemini-pro')
                self.__is_configured = True
        except ImportError:
            self.__is_configured = False

    def generate_ai_roadmap(self, raw_text: str, skills_found: List[str], intel: Dict[str, Any], role: str) -> Optional[str]:
        """Generates a hyper-personalized career roadmap authentically using Google Gemini."""
        if not self.__is_configured:
            return None
            
        try:
            missing_skills = intel.get("missing_high", []) + intel.get("missing_med", []) + intel.get("missing_low", [])
            weak_skills = intel.get("weak_skills", [])
            score = intel.get("score", 0)
            
            prompt = f"""You are an elite technical career mentor.

A candidate has the following raw profile context:
- Extracted Skills: {', '.join(skills_found) if skills_found else 'None'}
- Missing Target Skills: {', '.join(missing_skills) if missing_skills else 'None'}
- Functionally Weak Skills: {', '.join(weak_skills) if weak_skills else 'None'}
- Intended Target Role: {role}
- Algorithmic Readiness Score: {score}/100

Generate a highly personalized roadmap bridging them to mastery.

Requirements:
- Make it totally unique to this user based exactly on their flaws and strengths.
- Divide into phases or weeks securely using Markdown headings (e.g. ### Phase 1: Title).
- Explicitly encompass:
   - What to precisely learn
   - What system to practically build
   - How to deploy and practice the flow
- Make it definitively realistic and maximally actionable. No generic filler.
- Tone: Highly motivational but brutally honest regarding their limits.
"""
            response = self.__model.generate_content(prompt)
            return response.text
        except Exception as e:
            return None

    def generate_ai_resources(self, missing_skills: List[str], role: str) -> Optional[str]:
        """Generates hyper-specific educational resources using Google Gemini API."""
        if not self.__is_configured:
            return None
            
        if not missing_skills:
            return "You have absolutely no core technical gaps mapping to your role. No remedial learning is fundamentally needed!"
            
        try:
            prompt = f"""You are a senior hiring manager in the {role} field.
A candidate has precisely identified gaps in the following core technologies required for their pipeline: {', '.join(missing_skills)}

For each distinct skill, rigorously suggest:
- Best YouTube search query (exact powerful string to search)
- Best authoritative course name (specifically name drop premium Coursera, Udemy, or recognized platform modules)
- A highly realistic, localized practice method to acquire the skill practically

Make your suggestions highly specific, formatted strictly using clean Markdown with distinct dividers per skill. 
Use markdown Headers for the Skill name (e.g., ### SkillName). 
Do NOT write filler introductory or closing confirmation text. Stream output immediately.
"""
            response = self.__model.generate_content(prompt)
            return response.text
        except Exception as e:
            return None

    def ask_career_advisor(self, question: str, intel: Dict[str, Any], role: str, skills_found: List[str]) -> Optional[str]:
        """Conversational AI matrix allowing dynamic Q&A targeting candidate capability payload."""
        if not self.__is_configured:
            return "❌ Fatal Error: google.generativeai is not installed or configured."
            
        try:
            missing_skills = intel.get("missing_high", []) + intel.get("missing_med", []) + intel.get("missing_low", [])
            weak_skills = intel.get("weak_skills", [])
            score = intel.get("score", 0)
            level = intel.get("level", "Beginner")
            
            prompt = f"""You are an elite, brutally honest B2B technical career advisor.
Operate strictly leveraging the candidate's exact algorithmic capability pipeline payload:

====== TARGET CAPABILITY PAYLOAD ======
- Desired Domain Role: {role}
- Computed Readiness Output: {score}/100 ({level})
- Verified Skills Possessed: {', '.join(skills_found) if skills_found else 'None'}
- Missing Critical Constraints: {', '.join(missing_skills) if missing_skills else 'None'}
- Weak/Auxiliary Distraction Skills: {', '.join(weak_skills) if weak_skills else 'None'}
=======================================

USER QUESTION: "{question}"

ADVISOR INSTRUCTIONS:
- Answer based explicitly on the candidate's resume analysis properties.
- Be highly specific and profoundly helpful.
- DO NOT hallucinate capabilities they don't have.
- Maintain a highly actionable and concise operational tone. Do not provide disclaimers.
"""
            response = self.__model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Fatal System Exception (Gemini API): {repr(e)}"

    def generate_ai_confidence_insights(self, intel: Dict[str, Any], role: str) -> Optional[str]:
        """Generates an honest human-feeling executive evaluated evaluation and timeline metric."""
        if not self.__is_configured:
            return None
            
        try:
            missing_skills = intel.get("missing_high", []) + intel.get("missing_med", []) + intel.get("missing_low", [])
            weak_skills = intel.get("weak_skills", [])
            score = intel.get("score", 0)
            level = intel.get("level", "Beginner")
            
            prompt = f"""You are an empathetic yet firm B2B hiring professional reviewing a candidate for a {role} position.

Candidate operational metrics:
- Base Algorithmic Score: {score}/100 ({level})
- Major Missing Competencies: {', '.join(missing_skills) if missing_skills else 'None'}
- Technically Weak Areas: {', '.join(weak_skills) if weak_skills else 'None'}

Provide exactly TWO discrete short paragraphs properly spaced natively. Do not use bullet points or massive headers:

**Honest Evaluation:** Give a brutally candid but encouraging professional assessment directly tied to their flaws and strengths (e.g. "You possess solid foundational logic, but your lack of specific AWS routing constraints holds you back massively in modern pipelines."). 

**Timeline Estimate:** Provide a highly realistic and specific timeframe estimating when they will achieve Job-Ready deployment metrics if they work strictly on their weak areas (e.g. "You can fully reach Job-Ready thresholds in 2–3 months"). Defend the estimate logically.

Keep the structural tone supremely trustworthy, analytical, and highly human.
"""
            response = self.__model.generate_content(prompt)
            return response.text
        except Exception:
            return None
