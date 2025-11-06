# app.py - Streamlit Web Interface for Kelly AI Chatbot (LLM-Powered)

import streamlit as st
from datetime import datetime
import json
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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
    </style>
""", unsafe_allow_html=True)


# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'kelly' not in st.session_state:
    st.session_state.kelly = KellyScientist()

if 'api_provider' not in st.session_state:
    st.session_state.api_provider = "groq"

# Header
st.markdown('<div class="main-header">🤖 Kelly - The Skeptical AI Scientist</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Where every answer is a poem, and every claim is questioned (now powered by LLMs!)</div>', unsafe_allow_html=True)

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
    
    Now powered by **LLM APIs** for dynamic, context-aware responses!
    """)
    
    st.divider()
    
    # API Configuration
    st.header("🔧 API Settings")
    
    # Check for API keys
    has_groq = bool(os.getenv("GROQ_API_KEY"))
    has_hf = bool(os.getenv("HUGGINGFACE_API_KEY"))
    has_together = bool(os.getenv("TOGETHER_API_KEY"))
    has_openai = bool(os.getenv("OPENAI_API_KEY"))
    
    # API Provider Selection
    provider_options = []
    if has_groq:
        provider_options.append("groq")
    if has_hf:
        provider_options.append("huggingface")
    if has_together:
        provider_options.append("together")
    if has_openai:
        provider_options.append("openai")
    
    if not provider_options:
        st.error("⚠️ No API keys found! Please set at least one API key.")
        st.info("Set environment variable:\n- GROQ_API_KEY\n- HUGGINGFACE_API_KEY\n- TOGETHER_API_KEY\n- OPENAI_API_KEY")
        provider_options = ["groq"]  # Default fallback
    
    selected_provider = st.selectbox(
        "API Provider",
        provider_options,
        index=0,
        help="Select which LLM API to use"
    )
    
    # Show API status
    status_class = "active" if selected_provider in [p for p in ["groq", "huggingface", "together", "openai"] if eval(f"has_{p.replace('openai', 'openai')}")] else "inactive"
    status_text = "✅ API Key Found" if status_class == "active" else "❌ No API Key"
    st.markdown(f'<div class="api-status {status_class}">{status_text}</div>', unsafe_allow_html=True)
    
    # Model selection based on provider
    model_options = {
        "groq": [
            "llama-3.1-70b-versatile",
            "llama-3.1-8b-instant",
            "mixtral-8x7b-32768",
            "gemma2-9b-it"
        ],
        "huggingface": [
            "meta-llama/Llama-2-70b-chat-hf",
            "mistralai/Mixtral-8x7B-Instruct-v0.1",
            "microsoft/phi-2"
        ],
        "together": [
            "meta-llama/Llama-3-70b-chat-hf",
            "mistralai/Mixtral-8x7B-Instruct-v0.1",
            "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO"
        ],
        "openai": [
            "gpt-4",
            "gpt-3.5-turbo"
        ]
    }
    
    selected_model = st.selectbox(
        "Model",
        model_options.get(selected_provider, ["default"]),
        help="Select which model to use"
    )
    
    if st.button("🔄 Update API Settings"):
        st.session_state.kelly = KellyScientist(
            api_provider=selected_provider,
            model=selected_model
        )
        st.session_state.api_provider = selected_provider
        st.success(f"Updated to {selected_provider} with {selected_model}")
    
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
            lines_per_stanza=lines_per_stanza,
            api_provider=st.session_state.api_provider
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
    
    # Generate Kelly's response using the LLM
    with st.spinner(f"Kelly is composing her poetic response using {st.session_state.api_provider}..."):
        try:
            response = st.session_state.kelly.generate(user_question)
        except Exception as e:
            response = f"Error generating response: {str(e)}\n\nPlease check your API key and try again."
    
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
    <p>🤖 <strong>Technical Note:</strong> Kelly now uses LLM APIs (Groq, Hugging Face, Together AI, or OpenAI) 
    to generate dynamic, context-aware poetic responses while maintaining her analytical voice.</p>
    <p>⚡ <strong>Recommended:</strong> Use Groq for the fastest free responses!</p>
    <p>Built with ❤️ using Streamlit | © 2025 Kelly AI Scientist Chatbot</p>
</div>
""", unsafe_allow_html=True)
