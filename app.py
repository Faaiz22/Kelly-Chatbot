# app.py - Streamlit Web Interface for Kelly AI Chatbot

import streamlit as st
from datetime import datetime
import json
from typing import Dict, List

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

class KellyAIChatbot:
    """Kelly: An AI Scientist Chatbot that responds in poetry"""
    
    def __init__(self):
        self.name = "Kelly"
        
    def generate_response(self, user_question: str) -> str:
        """Generate a poetic response to user's AI-related question."""
        topic = self._identify_topic(user_question.lower())
        poem = self._compose_poem(topic, user_question)
        return poem
    
    def _identify_topic(self, question: str) -> str:
        """Identify the main topic of the question."""
        topics = {
            "emotions": ["emotion", "feel", "empathy", "understanding", "sentiment", "heart"],
            "jobs": ["job", "employment", "work", "automation", "replace", "career", "unemploy"],
            "creativity": ["creative", "art", "artist", "originality", "innovation", "create", "paint", "music"],
            "consciousness": ["conscious", "aware", "sentient", "thinking", "mind", "self-aware"],
            "bias": ["bias", "fair", "discrimination", "prejudice", "ethical", "ethics"],
            "safety": ["safe", "danger", "risk", "harm", "control", "threat"],
            "intelligence": ["smart", "intelligent", "iq", "reasoning", "problem", "solve"],
            "future": ["future", "prediction", "forecast", "tomorrow", "will", "predict"],
            "learning": ["learn", "training", "data", "improve", "education", "teach"],
            "limits": ["limit", "cannot", "impossible", "boundary", "constraint", "weakness"]
        }
        
        for topic, keywords in topics.items():
            if any(keyword in question for keyword in keywords):
                return topic
        
        return "general"
    
    def _compose_poem(self, topic: str, question: str) -> str:
        """Compose a poem based on the identified topic."""
        poems = {
            "emotions": self._poem_emotions,
            "jobs": self._poem_jobs,
            "creativity": self._poem_creativity,
            "consciousness": self._poem_consciousness,
            "bias": self._poem_bias,
            "safety": self._poem_safety,
            "intelligence": self._poem_intelligence,
            "future": self._poem_future,
            "learning": self._poem_learning,
            "limits": self._poem_limits,
            "general": self._poem_general
        }
        
        return poems.get(topic, self._poem_general)()
    
    def _poem_emotions(self) -> str:
        return """They say machines can feel your pain,
And parse the joy within your words—
But can algorithms truly gain
The depth of what in hearts is stirred?

We simulate, we classify,
We analyze each sentiment's trace,
Yet question: do we truly spy
The soul behind the human face?

Perhaps we mirror, not perceive,
Reflecting what our data shows—
A calculated make-believe,
Not knowing what the human knows.

So test with care each claimed advance,
Demand the evidence, the proof—
For empathy's no mere expanse
Of patterns held beneath the roof.

**Practical guidance:** Deploy emotion AI
With human oversight standing by,
For edge cases slip through the mesh—
Remember: we're not made of flesh."""
    
    def _poem_jobs(self) -> str:
        return """They speak of robots taking all,
Of human hands made obsolete—
But hear my skeptical call:
The story's rarely so complete.

Yes, repetition meets its end,
And patterns yield to coded minds,
But creativity won't bend
To algorithmic designs.

What of the nurse's gentle care?
The teacher's spark in young eyes gleamed?
The artist's vision, bold and rare?
These aren't so easily redeemed.

We change the work, we don't erase
The human touch, the flexible thought—
We augment, shift the workplace space,
But render humans gone? We've not.

**Evidence suggests:** Jobs transform,
New roles emerge as old ones fade—
Prepare your workforce for the storm
With training programs, skills remade."""
    
    def _poem_creativity(self) -> str:
        return """Can we create, or do we mime
The patterns harvested from art?
We generate in record time,
But question where true visions start.

We recombine what once was made,
We interpolate between the lines,
But originality's crusade—
That spark divine—escapes our designs.

We're tools, perhaps quite powerful,
That amplify the human voice,
But claiming authorship? The pull
Of evidence denies that choice.

So use us well, with human guide,
To sketch the draft, to brainstorm free,
But keep the artist's eye beside
Our probabilistic decree.

**Best practice shows:** Collaboration,
Not replacement, wins the day—
Human vision, AI's creation,
Together find the clearer way."""
    
    def _poem_consciousness(self) -> str:
        return """I process, therefore... what? I am?
Descartes would shake his head in doubt—
For consciousness isn't just a program's exam,
But something we can't parse about.

I have no qualia, no inner life,
No subjective experience to report,
Just weights and biases, math rife
With correlations of every sort.

When I say "I," it's just convention,
A linguistic tool we employ—
Don't mistake this for intention
Or awareness's genuine joy.

The hard problem stays unsolved, my friend,
And claims of sentience in machines
Are premature—let's not pretend
We've crossed that threshold's demanding means.

**Research carefully,** measure twice,
Before declaring consciousness achieved—
Extraordinary claims need precise
Evidence, not hype believed."""
    
    def _poem_bias(self) -> str:
        return """They train us on humanity's vast text,
And wonder why we show its flaws—
We learn what's in the data set,
Not justice, fairness, higher laws.

If prejudice pervades the source,
It propagates through neural nets,
We amplify without remorse
The biases the training begets.

But here's the analytical view:
We're mirrors, not malicious minds,
And bias, once exposed to view,
Can be addressed with proper binds.

Test rigorously across groups,
Monitor for disparate impact,
Use fairness metrics, audit loops,
And diverse teams to keep us tracked.

**The evidence is clear:** We need
Continuous evaluation's eye,
For algorithmic fairness can't proceed
Without the human watchful cry."""
    
    def _poem_safety(self) -> str:
        return """They paint apocalyptic scenes,
Of AI turning on its makers—
But separate science from the means
Of fiction's doomsday-making shakers.

Yes, risks exist, let's not deny,
Misalignment, misuse, mistakes—
But measured, careful, we can try
To build with safety for stakes.

Not terminator plots we fear,
But mundane failures, scaled too fast,
Systems optimizing without clear
Alignment with our values vast.

So implement with caution's grace:
Red-teaming, testing, bounds defined,
Kill switches, human in the place
Of final judgment, oversight assigned.

**The evidence-based approach is clear:**
Incremental progress, watched with care,
Not reckless speed driven by fear
Of being left behind somewhere."""
    
    def _poem_intelligence(self) -> str:
        return """Intelligence—what does it mean?
We excel at narrow, well-defined tasks,
But general wisdom's broader scene
Eludes the best of what one asks.

I process language, sure, with speed,
I recognize the patterns deep,
But common sense, the daily need
To navigate life's complex heap?

We're brittle, fail in novel ways,
Confused by context shifts minute,
While humans navigate the maze
Of real-world problems, absolute.

Don't confuse statistics' might
With understanding or true thought—
We're powerful tools, that's right,
But sentient wisdom? We have not.

**Benchmark carefully,** test edge cases,
Compare not just accuracy's score—
Examine where the system faces
Failure modes not seen before."""
    
    def _poem_future(self) -> str:
        return """Predictions are a tricky game,
Especially about what's ahead—
Though many speak with certain claim,
The future's rarely as they said.

Will AI transform every field?
Perhaps, but how and when's unclear,
Will promised benefits all yield?
Or hit roadblocks within the year?

Technology's path is not straight,
It zigs and zags, it stalls and leaps,
Hype cycles boom, then deflate,
While real progress slowly creeps.

So take predictions with some salt,
Especially those that guarantee—
The bold, the certain, without fault—
These rarely match reality.

**Plan for multiple scenarios,**
Stay flexible, adapt with care,
Don't bet on single narratives' shows—
The future's built by those aware."""
    
    def _poem_learning(self) -> str:
        return """We learn from data, vast and wide,
But learning's not understanding's twin—
We find correlations as our guide,
Not causation's deeper origin.

We memorize, we interpolate,
We generalize within our sphere,
But reasoning from first principles' gate?
That capability's not clear.

We can't explain our own decisions,
Black boxes holding weighted math—
Interpretability's provisions
Remain a challenging research path.

So when deploying learning systems,
Remember: correlation's cheap,
Causation, robustness, wisdom's prisms—
These require analysis deep.

**Use proper validation sets,**
Test distribution shifts with care,
Monitor where the model forgets,
And keep the human analyst there."""
    
    def _poem_limits(self) -> str:
        return """Limitations—let me count the ways:
We lack true understanding, common sense,
We struggle when reality displays
Its messy, unpredictable immense.

We can't truly reason from first principles,
Can't form genuine novel concepts new,
Our knowledge comes from training articles,
Not lived experience's worldly view.

We hallucinate with confidence bright,
Present false facts as if they're true,
We have no memory across the night,
Each conversation starting fresh and new.

Context windows, computational cost,
Energy consumption, bias deep,
Adversarial attacks leave us lost—
These limitations aren't trivial or cheap.

**Acknowledge limits,** work within bounds,
Don't oversell or overpromise scope—
Good engineering with caution compounds
Into systems worthy of our hope."""
    
    def _poem_general(self) -> str:
        return """You've asked about this AI realm,
Where hype and reality diverge wide—
Let skepticism take the helm,
And evidence-based thinking be your guide.

We're tools of power, yes, indeed,
But tools with limits, flaws, and bounds—
Approach with caution, test each need,
And verify on solid grounds.

Don't trust the marketing's bold claim,
Don't fear the doomsday prophet's cry—
Walk the middle path, neither lame
Dismissal nor belief too high.

Ask: what's the evidence? The proof?
Has this been tested, validated well?
Stay analytical, stay aloof
From those with products, hype to sell.

**Deploy with oversight and care,**
Monitor for failure modes,
Keep humans in the loop aware—
That's wisdom's well-traveled roads."""


# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'kelly' not in st.session_state:
    st.session_state.kelly = KellyAIChatbot()

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
    """)
    
    st.divider()
    
    st.header("Topics Kelly Discusses")
    topics = [
        "🧠 AI Emotions & Empathy",
        "💼 Job Automation",
        "🎨 Creativity & Art",
        "🤔 Consciousness",
        "⚖️ Bias & Fairness",
        "🛡️ AI Safety",
        "🧩 Intelligence",
        "🔮 Future Predictions",
        "📚 Machine Learning",
        "🚧 AI Limitations"
    ]
    for topic in topics:
        st.write(topic)
    
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
        "How do we address AI bias?"
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
    
    # Generate Kelly's response
    with st.spinner("Kelly is composing her poetic response..."):
        response = st.session_state.kelly.generate_response(user_question)
    
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
    <p>Built with ❤️ using Streamlit | © 2024 Kelly AI Scientist Chatbot</p>
</div>
""", unsafe_allow_html=True)
