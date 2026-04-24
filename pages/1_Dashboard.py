import streamlit as st
import sys
import os

# Add parent directory to path to import theme
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from theme import inject_professional_theme

def render_dashboard():
    st.set_page_config(page_title="Intelligence Dashboard", page_icon="📊", layout="wide")
    inject_professional_theme()

    if not st.session_state.get('analysis_complete', False):
        st.markdown("""
        <div class="glass-panel" style="text-align: center;">
            <p style="font-size: 3rem;">⚠️</p>
            <h2 style="color: #ef4444;">Pipeline Authorization Blocked</h2>
            <p style="color: #cbd5e1;">Return to the main terminal and securely inject a valid PDF payload first.</p>
        </div>
        """, unsafe_allow_html=True)
        return

    st.markdown('<p class="page-header anim-element">Intelligence <span class="hero-accent">Overview</span></p>', unsafe_allow_html=True)
    
    logic_engine = st.session_state['logic_engine']
    selected_role = st.session_state['selected_role']
    ai_insights = st.session_state.get('ai_insights_compiled')

    intel = logic_engine.intel
    score_val = intel["score"]
    level = intel["level"]
    
    if level == "Beginner":
        b_class, b_color = "red", "#ef4444"
    elif level == "Intermediate":
        b_class, b_color = "yellow", "#f59e0b"
    else:
        b_class, b_color = "green", "#10b981"

    # -----------------------------
    # TOP LEVEL METRICS
    # -----------------------------
    c1, c2, c3 = st.columns(3, gap="large")
    
    with c1:
        st.markdown(f"""
        <div class="glass-panel anim-element del-1" style="text-align: center; height: 260px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <p style="color: #94a3b8; text-transform: uppercase; font-weight: 700; font-size: 0.9rem; letter-spacing: 1px; margin-bottom: 20px;">Logic Engine Match</p>
            <div style="position: relative; width: 140px; height: 140px; border-radius: 50%; background: conic-gradient({b_color} {score_val * 3.6}deg, rgba(255,255,255,0.05) 0deg); display: flex; align-items: center; justify-content: center; box-shadow: 0 0 30px {b_color}33;">
                <div style="position: absolute; width: 120px; height: 120px; border-radius: 50%; background-color: #0d121f; display: flex; align-items: center; justify-content: center;">
                    <span style="font-size: 2.2rem; font-weight: 800; color: {b_color}; font-family: 'Outfit', sans-serif;">{score_val}<span style="font-size: 1.2rem; color:#64748b;">%</span></span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="glass-panel anim-element del-2" style="text-align: center; height: 260px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <p style="color: #94a3b8; text-transform: uppercase; font-weight: 700; font-size: 0.9rem; letter-spacing: 1px; margin-bottom: 20px;">Position Framework</p>
            <span class="badge {b_class}" style="font-size: 1.2rem; padding: 12px 24px;">{level} Tracker</span>
            <p style="margin-top:20px; font-size:0.9rem; color:#64748b; margin-bottom: 0;">Extrapolated from raw structural data points.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="glass-panel anim-element del-3" style="text-align: center; height: 260px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <p style="color: #94a3b8; text-transform: uppercase; font-weight: 700; font-size: 0.9rem; letter-spacing: 1px; margin-bottom: 20px;">Target Architecture</p>
            <div style="font-size: 1.8rem; font-weight: 700; color: #ffffff; font-family: 'Outfit', sans-serif; line-height: 1.2;">{selected_role}</div>
            <p style="margin-top:15px; font-size:0.9rem; color:#475569; margin-bottom: 0;">Active pipeline mapping parameters.</p>
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------
    # AI INSIGHT OVERRIDE
    # -----------------------------
    if ai_insights:
        st.markdown(f"""
        <div class="glass-panel anim-element del-4" style="margin-top: 30px; border-left: 4px solid #a855f7;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <span style="font-size: 1.5rem; margin-right: 10px;">✨</span>
                <h3 style="margin: 0; font-size: 1.3rem; color: #f8fafc;">Generative AI Executive Summary</h3>
            </div>
            <div style="color: #cbd5e1; font-size: 1.05rem; line-height: 1.6;">
                {ai_insights}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------
    # CORE COMPETENCY BREAKDOWN
    # -----------------------------
    st.markdown('<p style="font-size: 1.8rem; font-weight: 700; color: #ffffff; margin-top: 40px; margin-bottom: 20px;" class="anim-element">Diagnostic Subsystems</p>', unsafe_allow_html=True)
    
    t1, t2, t3 = st.columns(3, gap="large")
    
    def render_tags(skills, tag_class):
        if not skills:
            return '<p style="color: #64748b; font-style: italic; margin-top: 10px;">Null response detected.</p>'
        raw = ""
        for s in skills:
            raw += f'<span class="badge {tag_class}" style="margin: 4px; border-radius: 6px;">{s.title()}</span>'
        return f'<div style="margin-top: 15px;">{raw}</div>'

    with t1:
        st.markdown(f"""
        <div class="glass-panel anim-element del-1" style="height: 100%;">
            <h4 style="color: #10b981; margin-bottom: 5px;">Secure Integrations</h4>
            <p style="font-size: 0.85rem; color: #94a3b8; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 10px;">Hard dependencies met</p>
            {render_tags(intel.get("strong_skills", []), "green")}
        </div>
        """, unsafe_allow_html=True)

    with t2:
        st.markdown(f"""
        <div class="glass-panel anim-element del-2" style="height: 100%;">
            <h4 style="color: #f59e0b; margin-bottom: 5px;">Auxiliary Noise</h4>
            <p style="font-size: 0.85rem; color: #94a3b8; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 10px;">Weak peripheral skills</p>
            {render_tags(intel.get("weak_skills", []), "yellow")}
        </div>
        """, unsafe_allow_html=True)

    with t3:
        st.markdown(f"""
        <div class="glass-panel anim-element del-3" style="height: 100%;">
            <h4 style="color: #ef4444; margin-bottom: 5px;">Critical Failures</h4>
            <p style="font-size: 0.85rem; color: #94a3b8; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 10px;">Missing system requirements</p>
            {render_tags(logic_engine.missing_all_skills, "red")}
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_dashboard()
