import streamlit as st
import sys
import os

# Add parent directory to path to import theme
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from theme import inject_professional_theme

def render_advisor():
    st.set_page_config(page_title="AI Mentor", page_icon="💬", layout="wide")
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

    st.markdown('<p class="page-header anim-element">Live AI <span class="hero-accent">Architect Mentor</span></p>', unsafe_allow_html=True)
    
    if not st.session_state.get('gemini_api_key_valid', False):
        st.markdown("""
        <div class="glass-panel anim-element del-1" style="border-left: 5px solid #ef4444; margin-top: 20px;">
            <h3 style="color: #ef4444; margin-bottom: 10px;">⚠️ API Matrix Lock Detected</h3>
            <p style="color: #cbd5e1; font-size: 1.05rem;">A valid Gemini API Key must be injected on the Home page to initialize conversational frameworks.</p>
        </div>
        """, unsafe_allow_html=True)
        return

    st.markdown("""
    <div class="glass-panel anim-element del-1" style="padding: 20px 30px; margin-bottom: 40px; border-left: 5px solid #3b82f6;">
        <p style="color: #cbd5e1; font-size: 1.1rem; margin: 0;">Pose complex strategic questions tracking heavily against your identified matrix capabilities. The AI natively understands your uploaded profile context.</p>
    </div>
    """, unsafe_allow_html=True)

    # Chat UI styling overrides
    st.markdown("""
    <style>
    .stChatMessage {
        background-color: transparent !important;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }
    div[data-testid="chatAvatarIcon-user"] { background-color: #3b82f6 !important; }
    div[data-testid="chatAvatarIcon-assistant"] { background-color: #a855f7 !important; }
    .stChatMessage[data-testid="stChatMessage"]:nth-child(even) {
        background: rgba(139, 92, 246, 0.05) !important;
        border: 1px solid rgba(139, 92, 246, 0.1);
    }
    .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
        background: rgba(59, 130, 246, 0.05) !important;
        border: 1px solid rgba(59, 130, 246, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

    # Render History
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    selected_role = st.session_state['selected_role']
    logic_engine = st.session_state['logic_engine']
    ai_engine = st.session_state['ai_engine']
    processor = st.session_state['processor']

    if user_query := st.chat_input(f"E.g., Based on my gaps, am I practically ready for {selected_role}?"):
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)
            
        with st.chat_message("assistant"):
            with st.spinner("🤖 Formulating strategic actionable advice..."):
                response = ai_engine.ask_career_advisor(
                    question=user_query, 
                    intel=logic_engine.intel, 
                    role=selected_role, 
                    skills_found=processor.skills_found
                )
                if response:
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                else:
                    st.error("❌ Fatal System Response. Validate active API Keys and quotas.")

if __name__ == "__main__":
    render_advisor()
