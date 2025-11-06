# app.py - Streamlit Web Interface for Kelly AI Chatbot (LLM-Powered)

import streamlit as st
from datetime import datetime
import json
import sys
import os

# Add the package to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the actual Kelly implementation
from kelly_ai_scientist.kelly import KellyScientist

# Page configuration
st.set_page_config(
    page_title="Kelly - AI Scientist Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1E3A8A;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #64748B;
        margin-bottom: 2rem;
    }
    .poem-box {
        background-color: #F8FAFC;
        border-left: 4px solid #3B82F6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        font-family: 'Georgia', serif;
        line-height: 1.8;
        margin: 1rem 0;
        white-space: pre-line;
    }
    .user-message {
        background-color: #EFF6FF;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .stButton>button {
        width: 100%;
    }
    .api-status {
        padding: 0.5rem;
        border-radius: 0.25rem;
        margin: 0.5rem 0;
        font-size: 0.9rem;
    }
    .api-status.active {
        background-color: #D1FAE5;
        color: #065F46;
    }
    .api-status.inactive {
        background-color: #FEE2E2;
        color: #991B1B;
    }
    .info-box {
        background-color: #EFF6FF;
        border-left: 4px solid #3B82F6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)


# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'api_key' not in st.session_state:
    st.session_state.api_key = ""

if 'kelly' not in st.session_state:
    st.session_state.kelly = None

# Header
st.markdown('<div class="main-header">🤖 Kelly - The Skeptical AI Scientist</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Where every answer is a poem, and every claim is questioned (powered by Groq LLM!)</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("🔑 API Configuration")
    
    # Info box about Groq
    st.markdown("""
    <div class="info-box">
        <strong>📘 Get Your Free Groq API Key:</strong><br>
        1. Visit <a href="https://console.groq.com" target="_blank">console.groq.com</a><br>
        2. Sign up (free, no credit card needed)<br>
        3. Go to API Keys section<br>
        4. Create a new key and paste it below
    </div>
    """, unsafe_allow_html=True)
    
    # API Key input
    api_key_input = st.text_input(
        "Groq API Key",
        value=st.session_state.api_key,
        type="password",
        placeholder="gsk_...",
        help="Enter your Groq API key. It will be stored only for this session."
    )
    
    # Update API key
    if api_key_input != st.session_state.api_key:
        st.session_state.api_key = api_key_input
        if api_key_input:
            st.session_state.kelly = KellyScientist(
                api_key=api_key_input,
                api_provider="groq"
            )
    
    # Show API status
    if st.session_state.api_key:
        st.markdown('<div class="api-status active">✅ API Key Set</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="api-status inactive">❌ No API Key - Using Fallback Mode</div>', unsafe_allow_html=True)
        st.warning("⚠️ Without an API key, Kelly will use basic template responses.")
    
    # Model selection
    if st.session_state.api_key:
        st.subheader("Model Settings")
        selected_model = st.selectbox(
            "Choose Model",
            [
                "llama-3.1-70b-versatile",
                "llama-3.1-8b-instant",
                "mixtral-8x7b-32768",
                "gemma2-9b-it"
            ],
            help="Llama 70B is smartest but slower. 8B is fastest."
        )
        
        if st.button("🔄 Update Model"):
            st.session_state.kelly = KellyScientist(
                api_key=st.session_state.api_key,
                api_provider="groq",
                model=selected_model
            )
            st.success(f"Updated to {selected_model}")
    
    st.divider()
    
    st.header("About Kelly")
    st.write("""
    **Kelly** is an AI scientist chatbot who responds to questions about artificial intelligence 
    in poetic verse. Her responses are:
    
    - 📊 **Skeptical & Analytical**
    - 🔬 **Evidence-based**
    - 🎭 **Professionally poetic**
    - ⚠️ **Highlighting AI limitations**
    
    Powered by **Groq's LLM API** for dynamic, context-aware responses!
    """)
    
    st.divider()
    
    st.header("Common Topics")
    topics = [
        "🧠 AI Emotions & Empathy",
        "💼 Job Automation & Labor",
        "🎨 Creativity & Art",
        "🤔 Consciousness & Sentience",
        "⚖️ Bias & Fairness",
        "🛡️ AI Safety & Risks",
        "🧩 Intelligence & Reasoning",
        "🔮 Future Predictions",
        "📚 Machine Learning",
        "🚧 AI Limitations"
    ]
    for topic in topics:
        st.write(topic)
    
    st.divider()
    
    # Poem structure settings
    st.header("Poem Structure")
    stanzas = st.slider("Number of stanzas", 2, 6, 4)
    lines_per_stanza = st.slider("Lines per stanza", 3, 6, 4)
    
    if st.button("Update Structure"):
        if st.session_state.api_key:
            st.session_state.kelly = KellyScientist(
                stanzas=stanzas,
                lines_per_stanza=lines_per_stanza,
                api_key=st.session_state.api_key,
                api_provider="groq"
            )
        else:
            st.session_state.kelly = KellyScientist(
                stanzas=stanzas,
                lines_per_stanza=lines_per_stanza
            )
        st.success("Poem structure updated!")
    
    st.divider()
    
    # Conversation controls
    st.header("Conversation Controls")
    
    if st.button("📝 Download Chat History"):
        if st.session_state.chat_history:
            chat_json = json.dumps(st.session_state.chat_history, indent=2)
            st.download_button(
                label="Download JSON",
                data=chat_json,
                file_name=f"kelly_conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
        else:
            st.warning("No conversation history to download")
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()
    
    st.divider()
    
    st.header("Example Questions")
    example_questions = [
        "Can AI understand human emotions?",
        "Will AI replace all jobs?",
        "Is AI truly creative?",
        "Can machines become conscious?",
        "How do we address AI bias?",
        "What are AI's limitations?",
        "How intelligent is AI really?"
    ]
    
    for i, question in enumerate(example_questions):
        if st.button(question, key=f"example_{i}"):
            st.session_state.current_question = question

# Main chat interface
st.header("Chat with Kelly")

# Show warning if no API key
if not st.session_state.api_key:
    st.info("💡 **Tip:** Add your Groq API key in the sidebar to get dynamic AI-generated poems! Without it, Kelly uses basic templates.")

# Display chat history
for i, message in enumerate(st.session_state.chat_history):
    if message['role'] == 'user':
        with st.container():
            st.markdown(f'<div class="user-message"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
    else:
        with st.container():
            st.markdown(f'<div class="poem-box">{message["content"]}</div>', unsafe_allow_html=True)

# Input area
user_question = st.text_input(
    "Ask Kelly about AI:",
    value=st.session_state.get('current_question', ''),
    placeholder="e.g., Can AI truly understand emotions?",
    key="user_input"
)

col1, col2 = st.columns([3, 1])

with col1:
    send_button = st.button("🚀 Send Question", type="primary", use_container_width=True)

with col2:
    clear_input = st.button("🔄 Clear", use_container_width=True)

# Handle button clicks
if clear_input:
    if 'current_question' in st.session_state:
        del st.session_state.current_question
    st.rerun()

if send_button and user_question:
    # Add user message to history
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_question,
        "timestamp": datetime.now().isoformat()
    })
    
    # Initialize Kelly if not already done
    if st.session_state.kelly is None:
        if st.session_state.api_key:
            st.session_state.kelly = KellyScientist(
                api_key=st.session_state.api_key,
                api_provider="groq"
            )
        else:
            st.session_state.kelly = KellyScientist()
    
    # Generate Kelly's response
    with st.spinner("Kelly is composing her poetic response..."):
        try:
            response = st.session_state.kelly.generate(user_question)
        except Exception as e:
            response = f"⚠️ Error generating response: {str(e)}\n\nPlease check your API key and try again."
            st.error(f"Error: {str(e)}")
    
    # Add Kelly's response to history
    st.session_state.chat_history.append({
        "role": "kelly",
        "content": response,
        "timestamp": datetime.now().isoformat()
    })
    
    # Clear the current question
    if 'current_question' in st.session_state:
        del st.session_state.current_question
    
    # Rerun to display new messages
    st.rerun()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #64748B; font-size: 0.9rem;'>
    <p>💡 <strong>Remember:</strong> Kelly's responses are skeptical by design. She questions broad claims 
    and highlights limitations to encourage critical thinking about AI technology.</p>
    <p>🤖 <strong>Technical Note:</strong> Kelly uses Groq's LLM API to generate dynamic, context-aware 
    poetic responses while maintaining her analytical voice.</p>
    <p>⚡ <strong>Free & Fast:</strong> Groq offers generous free tier with lightning-fast responses!</p>
    <p>🔒 <strong>Privacy:</strong> Your API key is stored only in your browser session and never logged.</p>
    <p>Built with ❤️ using Streamlit | © 2025 Kelly AI Scientist Chatbot</p>
</div>
""", unsafe_allow_html=True)
