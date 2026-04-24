"""
app.py

Central Entry Point for the Professional AI Career Readiness System.
Handles PDF injection, Global Session State instantiation, and routing configuration.
Designed with advanced Glassmorphism UI integration.
"""

import streamlit as st
from backend import ResumeProcessor, CareerLogicEngine, GenerativeAIEngine
from data import PREDEFINED_SKILLS, JOB_ROLES
from theme import inject_professional_theme

def initialize_session_state():
    """Ensure all critical variables exist in session state."""
    state_defaults = {
        'processor': None,
        'logic_engine': None,
        'ai_engine': None,
        'selected_role': None,
        'analysis_complete': False,
        'gemini_api_key_valid': False,
        'ai_roadmap_compiled': None,
        'ai_resources_compiled': None,
        'ai_insights_compiled': None,
        'messages': []
    }
    for key, val in state_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def main():
    # Streamlit config MUST be the first command
    st.set_page_config(page_title="Career AI | Professional", page_icon="🎯", layout="wide", initial_sidebar_state="expanded")
    
    # Inject ultimate theme styling
    inject_professional_theme()
    initialize_session_state()
    
    # -----------------------------
    # HERO SECTION
    # -----------------------------
    ccol1, ccol2, ccol3 = st.columns([1, 4, 1])
    with ccol2:
        st.markdown('<div style="text-align: center; margin-top: 30px;" class="anim-element">', unsafe_allow_html=True)
        st.markdown('<p class="hero-title">Career <span class="hero-accent">Intelligence</span></p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 1.25rem; color: #94a3b8; font-weight: 400; margin-bottom: 40px;">Upload your professional profile to generate a highly personalized, AI-driven career deployment matrix.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # -----------------------------
    # CONTROL PANEL (SIDEBAR)
    # -----------------------------
    with st.sidebar:
        st.markdown('<div style="padding: 10px 0;"><h3 style="color: #a855f7; margin-bottom: 20px;">⚙️ Engine Settings</h3></div>', unsafe_allow_html=True)
        roles = list(JOB_ROLES.keys()) if isinstance(JOB_ROLES, dict) else ["General Professional"]
        selected_role = st.selectbox("Target Architecture Model", roles)
        
        st.markdown("<hr style='border-color: rgba(255,255,255,0.05);'>", unsafe_allow_html=True)
        
        st.markdown('<div style="margin-bottom: 15px;"><h4 style="color: #cbd5e1;">🤖 AI Overdrive (Optional)</h4></div>', unsafe_allow_html=True)
        gemini_api_key = st.text_input("Gemini API Key", type="password", help="Providing a Google Gemini key unlocks ultra-personalized insights and Generative AI chat.", placeholder="Enter API Key...")
        
    # -----------------------------
    # MAIN UPLOAD MATRIX
    # -----------------------------
    col_left, col_mid, col_right = st.columns([1, 6, 1])
    
    with col_mid:
        st.markdown('<div class="glass-panel anim-element del-1">', unsafe_allow_html=True)
        
        if not st.session_state['analysis_complete']:
            st.markdown('<h3 style="margin-bottom: 20px;">📄 Primary Document Injection</h3>', unsafe_allow_html=True)
            uploaded_file = st.file_uploader("Drop your PDF Resume securely here", type=["pdf"])
            
            if st.button("🚀 Initialize Pipeline Evaluation", use_container_width=True):
                if not uploaded_file:
                    st.error("⚠️ Halted: A PDF document is required to ignite the analysis sequence.")
                else:
                    with st.spinner("⏳ Vectorizing Document Elements..."):
                        try:
                            # 1. Processing
                            processor = ResumeProcessor()
                            processor.ingest_pdf(uploaded_file)
                            processor.extract_skills(list(PREDEFINED_SKILLS))
                            
                            # 2. Logic Mapping
                            role_reqs = JOB_ROLES.get(selected_role, {"high_priority": [], "medium_priority": [], "low_priority": []})
                            logic_engine = CareerLogicEngine(processor.raw_text, processor.skills_found, role_reqs, selected_role)
                            logic_engine.evaluate()
                            
                            st.session_state['processor'] = processor
                            st.session_state['logic_engine'] = logic_engine
                            st.session_state['selected_role'] = selected_role
                            st.session_state.messages = []
                            
                            # 3. AI Instantiation
                            ai_engine = GenerativeAIEngine(gemini_api_key.strip()) if gemini_api_key else None
                            st.session_state['ai_engine'] = ai_engine
                            st.session_state['gemini_api_key_valid'] = True if ai_engine else False
                            
                            ai_roadmap_compiled = None
                            ai_resources_compiled = None
                            ai_insights_compiled = None
                            
                            if ai_engine:
                                with st.spinner("🤖 Communicating with Gemini LLM Clusters..."):
                                    target_skills = logic_engine.missing_all_skills + logic_engine.weak_skills
                                    ai_insights_compiled = ai_engine.generate_ai_confidence_insights(logic_engine.intel, selected_role)
                                    ai_roadmap_compiled = ai_engine.generate_ai_roadmap(
                                        processor.raw_text, 
                                        processor.skills_found, 
                                        logic_engine.intel, 
                                        selected_role
                                    )
                                    if target_skills:
                                         ai_resources_compiled = ai_engine.generate_ai_resources(target_skills, selected_role)
                            
                            st.session_state['ai_insights_compiled'] = ai_insights_compiled
                            st.session_state['ai_roadmap_compiled'] = ai_roadmap_compiled
                            st.session_state['ai_resources_compiled'] = ai_resources_compiled
                            st.session_state['analysis_complete'] = True
                            st.rerun()

                        except ValueError as ve:
                            st.error(f"❌ Input Integrity Failure: {str(ve)}")
                        except Exception as e:
                            st.error(f"❌ Core Exception Failure: {str(e)}")
                            
        else:
            # Render completion state
            score = st.session_state['logic_engine'].intel["score"]
            st.markdown(f"""
            <div style="text-align: center; padding: 20px 0;">
                <div style="font-size: 4rem; margin-bottom: 20px;">✅</div>
                <h2 style="color: #10b981; margin-bottom: 10px;">Deployment Subsystem Authorized</h2>
                <p style="color: #94a3b8; font-size: 1.15rem; margin-bottom: 30px;">
                    Resume integrity verified. Predictive algorithm matched the profile at <strong><span style="color:#ffffff;">{score}%</span></strong> accuracy against <strong>{st.session_state['selected_role']}</strong> constraints.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([1, 2, 1])
            with c2:
                if st.button("🔄 Reset Global State & Reboot", use_container_width=True):
                    for key in list(st.session_state.keys()):
                        del st.session_state[key]
                    st.rerun()
            
            st.markdown('<p style="text-align: center; color: #3b82f6; font-weight: 500; font-size: 1.1rem; margin-top: 20px;">Use the Sidebar Tabs to navigate your Intelligence Dashboards.</p>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
