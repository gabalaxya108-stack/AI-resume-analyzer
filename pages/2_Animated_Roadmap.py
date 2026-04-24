import streamlit as st
import sys
import os

# Add parent directory to path to import theme
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from theme import inject_professional_theme

def render_roadmap():
    st.set_page_config(page_title="AI Roadmap", page_icon="🗺️", layout="wide")
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

    st.markdown('<p class="page-header anim-element">Interactive <span class="hero-accent">Roadmap</span></p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#94a3b8; font-size:1.15rem; margin-bottom: 40px;" class="anim-element del-1">Track sequential progress across your structured target capability nodes.</p>', unsafe_allow_html=True)
    
    # Initialize checklist state cleanly
    if 'roadmap_checklist' not in st.session_state:
        st.session_state['roadmap_checklist'] = {}
        
    ai_roadmap = st.session_state.get('ai_roadmap_compiled')
    logic_engine = st.session_state['logic_engine']
    algorithmic_roadmap = logic_engine.roadmap

    if ai_roadmap:
        st.markdown('<div class="anim-element del-2" style="margin-bottom: 40px;">', unsafe_allow_html=True)
        with st.expander("🤖 View Generative AI Pipeline Analysis Context"):
            st.markdown(f'<div style="color: #cbd5e1; font-size: 1.05rem; padding: 10px;">{ai_roadmap}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
            
    # Draw Roadmap Timeline
    st.markdown('<div class="timeline-container anim-element del-3">', unsafe_allow_html=True)
    
    theme_colors = ["blue", "purple", "cyan"]
    hex_colors = {"blue": "#3b82f6", "purple": "#a855f7", "cyan": "#0ea5e9"}
    
    for phase_idx, (phase_title, topics) in enumerate(algorithmic_roadmap.items()):
        # Phase Header
        c_theme = theme_colors[phase_idx % len(theme_colors)]
        c_hex = hex_colors[c_theme]
        
        st.markdown(f'''
        <div style="margin-top: 50px; margin-bottom: 20px; display: inline-block;">
            <div style="background: rgba(17, 24, 39, 0.9); border: 1px solid rgba(255,255,255,0.1); border-left: 5px solid {c_hex}; padding: 12px 24px; border-radius: 12px; font-weight: 800; font-size: 1.4rem; color: #f8fafc; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
                {phase_title}
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        if isinstance(topics, list):
            for topic_idx, topic_data in enumerate(topics):
                if isinstance(topic_data, dict):
                    topic_name = topic_data.get("topic", "Topic")
                    items = topic_data.get("items", [])
                    
                    # Node Box
                    st.markdown(f"""
                        <div class="timeline-node">
                            <div style="background: rgba(17, 24, 39, 0.6); backdrop-filter: blur(16px); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 20px 30px; margin-left: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); transition: all 0.3s;">
                                <h3 style="color: #ffffff; margin-bottom: 10px; font-size: 1.3rem;">{topic_name}</h3>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Mount tracking checkboxes underneath
                    with st.container():
                        st.markdown("<div style='padding-left: 70px; margin-bottom: 40px; margin-top: -20px;'>", unsafe_allow_html=True)
                        for item in items:
                            unique_key = f"chk_{phase_idx}_{topic_idx}_{item}"
                            if unique_key not in st.session_state['roadmap_checklist']:
                                st.session_state['roadmap_checklist'][unique_key] = False
                                
                            val = st.checkbox(item, value=st.session_state['roadmap_checklist'][unique_key], key=unique_key)
                            st.session_state['roadmap_checklist'][unique_key] = val
                        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    render_roadmap()
