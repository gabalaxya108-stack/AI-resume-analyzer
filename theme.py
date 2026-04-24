"""
theme.py

Global CSS Injector handling maximum aesthetic overrides for Streamlit.
Unlocks Glassmorphism, Micro-animations, and full-screen kinetic backgrounds.
"""
import streamlit as st

def inject_professional_theme():
    """Injects highest-tier SaaS styling into the Streamlit ecosystem."""
    
    st.markdown("""
        <style>
        /* Modern Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');
        
        * { font-family: 'Inter', sans-serif !important; }
        h1, h2, h3, h4, h5, h6, .hero-title, .metric-val-txt, .page-header { 
            font-family: 'Outfit', sans-serif !important; 
        }

        /* Ultimate Dark Theme Background */
        .stApp { 
            background-color: #030712; /* Deep Void Black */
            color: #f8fafc;
        }
        
        /* Hide default Streamlit fluff */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden; height: 0px !important;}
        footer {visibility: hidden;}
        
        /* Tighten layout constraints */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 5rem !important;
            max-width: 1400px;
        }

        /* Complex Kinetic Background Simulation */
        .stApp::before, .stApp::after {
            content: '';
            position: fixed;
            width: 50vw;
            height: 50vw;
            border-radius: 50%;
            filter: blur(140px);
            opacity: 0.15;
            z-index: -1;
            pointer-events: none;
            animation: ultimateFloat 25s infinite alternate cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .stApp::before {
            background: radial-gradient(circle, #8b5cf6, #3b0764); /* Purple Core */
            top: -20%; left: -10%;
        }
        
        .stApp::after {
            background: radial-gradient(circle, #0ea5e9, #082f49); /* Cyan Base */
            bottom: -20%; right: -10%;
            animation-delay: -12s;
        }

        @keyframes ultimateFloat {
            0% { transform: translate(0, 0) scale(1) rotate(0deg); }
            33% { transform: translate(25vw, 15vh) scale(1.3) rotate(45deg); opacity: 0.25; }
            66% { transform: translate(-15vw, 40vh) scale(0.8) rotate(-20deg); opacity: 0.1; }
            100% { transform: translate(15vw, -30vh) scale(1.2) rotate(15deg); opacity: 0.2; }
        }

        /* True Glassmorphism Design System */
        .glass-panel {
            background: rgba(17, 24, 39, 0.4);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            border-left: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            padding: 30px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
        }
        
        .glass-panel:hover {
            transform: translateY(-5px) scale(1.01);
            border: 1px solid rgba(139, 92, 246, 0.3);
            box-shadow: 0 35px 60px -15px rgba(139, 92, 246, 0.15);
        }

        /* Glow effects for cards */
        .glass-panel::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.8), transparent);
            opacity: 0;
            transition: opacity 0.5s ease;
        }
        .glass-panel:hover::before {
            opacity: 1;
        }

        /* Typography Essentials */
        .stMarkdown, p, span, div { color: #cbd5e1; }
        h1, h2, h3, h4, h5, h6 { color: #f8fafc !important; font-weight: 700 !important; }
        
        .hero-title {
            font-size: 5rem;
            font-weight: 800;
            line-height: 1.1;
            letter-spacing: -0.04em;
            margin-bottom: 20px;
            background: linear-gradient(to right, #ffffff, #94a3b8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .hero-accent {
            background: linear-gradient(135deg, #a855f7 0%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: relative;
            display: inline-block;
        }

        /* Dynamic Stagger Animations for UI mounting */
        @keyframes slideUpFade {
            0% { opacity: 0; transform: translateY(30px) scale(0.95); filter: blur(10px); }
            100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0px); }
        }
        
        .anim-element {
            opacity: 0;
            animation: slideUpFade 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        .del-1 { animation-delay: 0.1s; }
        .del-2 { animation-delay: 0.25s; }
        .del-3 { animation-delay: 0.4s; }
        .del-4 { animation-delay: 0.55s; }

        /* Sleek Button Overrides */
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #8b5cf6 0%, #3b82f6 100%);
            border: none;
            color: white;
            padding: 16px 32px;
            border-radius: 12px;
            font-weight: 600;
            font-size: 1.1rem;
            letter-spacing: 0.5px;
            box-shadow: 0 10px 20px -5px rgba(139, 92, 246, 0.4);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            width: 100%;
            cursor: pointer;
        }
        div.stButton > button:first-child:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 15px 25px -5px rgba(139, 92, 246, 0.6);
            background: linear-gradient(135deg, #a855f7 0%, #60a5fa 100%);
        }
        div.stButton > button:first-child:active {
            transform: translateY(0) scale(0.98);
        }

        /* Sidebar Glassification */
        section[data-testid="stSidebar"] {
            background-color: rgba(3, 7, 18, 0.7) !important;
            backdrop-filter: blur(30px);
            border-right: 1px solid rgba(255,255,255,0.05);
        }
        section[data-testid="stSidebar"] hr {
            border-color: rgba(255,255,255,0.05) !important;
        }
        
        /* Inputs & Dropdowns */
        .stTextInput input, div[data-baseweb="select"] > div {
            background-color: rgba(17, 24, 39, 0.5) !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 12px !important;
            color: #f8fafc !important;
            padding: 12px 16px;
            transition: all 0.3s ease;
        }
        .stTextInput input:focus, div[data-baseweb="select"] > div:hover {
            background-color: rgba(17, 24, 39, 0.8) !important;
            border-color: #8b5cf6 !important;
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2) !important;
        }

        /* Upload Area */
        div[data-testid="stFileUploader"] {
            background-color: rgba(17, 24, 39, 0.3);
            border: 2px dashed rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 30px;
            transition: all 0.4s ease;
        }
        div[data-testid="stFileUploader"]:hover {
            border-color: #a855f7;
            background-color: rgba(168, 85, 247, 0.05);
            transform: scale(1.02);
        }
        
        /* Loading Spinners */
        .stSpinner > div > div {
            border-top-color: #a855f7 !important;
        }
        
        /* Timeline Specific Styling (for roadmap) */
        .timeline-container {
            position: relative;
            padding-left: 40px;
            margin: 40px 0;
        }
        .timeline-container::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            background: linear-gradient(to bottom, #8b5cf6, #38bdf8, transparent);
            border-radius: 4px;
        }
        .timeline-node {
            position: relative;
            margin-bottom: 30px;
        }
        .timeline-node::before {
            content: '';
            position: absolute;
            left: -46px;
            top: 0;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #030712;
            border: 4px solid #a855f7;
            box-shadow: 0 0 15px rgba(168, 85, 247, 0.6);
            z-index: 10;
        }

        /* Badges */
        .badge {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 30px;
            font-size: 0.9rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }
        .badge.green { background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.3); }
        .badge.yellow { background: rgba(245, 158, 11, 0.15); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.3); }
        .badge.red { background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3); }
        .badge.blue { background: rgba(59, 130, 246, 0.15); color: #3b82f6; border: 1px solid rgba(59, 130, 246, 0.3); }

        </style>
    """, unsafe_allow_html=True)
