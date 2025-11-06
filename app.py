# app.py - Streamlit Web Interface for Kelly AI Chatbot

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
    </style>
""", unsafe_allow_html=True)


# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'kelly' not in st.session_state:
    st.session_state.kelly = KellyScientist()

# Header
st.markdown('<div class="main-header">🤖 Kelly - The Skeptical AI Scientist</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Where every answer is a poem, and every claim is questioned</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("About Kelly")
    st.write("""
    **Kelly** is an AI scientist chatbot who responds to questions about artificial intelligence 
    in poetic verse. Her responses are:
    
    - 📊 **Skeptical & Analytical**
    - 🔬 **Evidence-based**
    - 🎭 **Professionally poetic**
    - ⚠️ **Highlighting AI limitations**
    
    Kelly uses a template-based system to ensure every response includes:
    1. Skeptical questioning of broad AI claims
    2. Clear articulation of AI limitations
    3. Practical, evidence-based suggestions
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

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    send_button = st.button("🚀 Send Question", type="primary", use_container_width=True)

with col2:
    clear_input = st.button("🔄 Clear Input", use_container_width=True)

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
    
    # Generate Kelly's response using the actual implementation
    with st.spinner("Kelly is composing her poetic response..."):
        response = st.session_state.kelly.generate(user_question)
    
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
    <p>⚙️ <strong>Technical Note:</strong> Kelly uses a deterministic template-based system, not a 
    large language model. This ensures consistent, evidence-based responses.</p>
    <p>Built with ❤️ using Streamlit | © 2025 Kelly AI Scientist Chatbot</p>
</div>
""", unsafe_allow_html=True)
