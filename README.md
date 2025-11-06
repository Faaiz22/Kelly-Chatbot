# Kelly — AI Scientist Chatbot 

A lightweight chatbot powered by **Groq's free LLM API** that answers **only in poems** with a **skeptical, analytical, and professional** tone.

Every poem:
1. Questions broad claims about AI
2. Highlights limitations of AI technology
3. Offers practical, evidence-based suggestions

##  New: LLM-Powered!

Kelly now uses **Groq's free API** to generate dynamic, context-aware poetic responses instead of templates!

-  **Lightning fast** responses (2-5 seconds)
-  **Completely free** (~14,400 requests/day)
-  **Unique poems** for every question
-  **Truly understands** context and nuance
-  **Secure** - API key stored only in your session

## Quick Start

### 1. Get Free Groq API Key (30 seconds)

1. Visit https://console.groq.com
2. Sign up (no credit card required)
3. Create API key from dashboard
4. Copy your key (starts with `gsk_`)

### 2. Run the App

```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

### 3. Enter API Key

Open the Streamlit app in your browser and paste your API key in the sidebar. Start chatting!

## Features

-  **AI-Generated Poetry** - Unique, context-aware poems every time
-  **Evidence-based responses** - Grounded in AI research limitations
-  **Skeptical tone** - Questions hype and marketing claims
-  **Context-aware** - Understands your specific questions
-  **Customizable structure** - Configure stanzas and lines
-  **Web interface** - Interactive Streamlit UI
-  **Privacy-focused** - API key stored only in session
-  **Fallback mode** - Works without API (basic templates)

## Example

**Input:** "Can AI truly understand human emotions?"

**Kelly's Response:**
```
Tell me again—how certain are we that algorithms grasp sorrow?
What does a neural net know of the weight of grief?
When loss isn't labeled, when context shifts with culture,
The model sees patterns, not the person behind the pain.

Sentiment analysis maps valence onto axes we designed,
But joy and rage aren't points—they're landscapes, moving targets.
We train on tweets and reviews, then deploy on trauma—
The gap between data and depth grows wider than we admit.

Without lived experience, correlation mimics understanding,
Benchmarks rise, yet empathy remains beyond the gradient.
We confuse prediction with perception, accuracy with insight,
And forget that feeling isn't just a feature to extract.

Run tests on edge cases where labels blur and context matters.
Build systems with humility, acknowledging what models miss.
Let uncertainty be explicit; let human judgment remain central.
The best AI admits what it cannot know about the heart.
```

## How It Works

Kelly uses **Groq's LLM API** with a carefully crafted system prompt to ensure every response:
- Maintains skeptical, analytical tone
- Questions broad AI claims
- Highlights specific limitations
- Provides practical suggestions
- Follows poetic structure

## Customization

```python
from kelly_ai_scientist.kelly import KellyScientist

# Custom poem structure
kelly = KellyScientist(
    api_key="your-groq-key",
    stanzas=5,
    lines_per_stanza=3
)

# Different model
kelly = KellyScientist(
    api_key="your-groq-key",
    model="llama-3.1-8b-instant"  # Faster
)

# Generate poem
poem = kelly.generate("How intelligent is AI?")
print(poem)
```

## Available Models

| Model | Speed | Quality | Best For |
|-------|-------|---------|----------|
| llama-3.1-70b-versatile | Medium | Highest | Best poems |
| llama-3.1-8b-instant | Fastest | Good | Quick responses |
| mixtral-8x7b-32768 | Medium | High | Long context |
| gemma2-9b-it | Fast | Good | Efficiency |

## Topics Covered

-  AI Emotions & Empathy
-  Job Automation & Labor
-  Creativity & Originality  
-  Consciousness & Sentience
-  Bias & Fairness
-  AI Safety & Risks
-  Intelligence & Reasoning
-  Future Predictions
-  Machine Learning
-  AI Limitations
- **And any AI-related topic!**

## Why Groq?

-  **Free tier**: ~14,400 requests/day
-  **Fast**: Responses in 2-5 seconds
-  **No credit card**: Sign up with email only
-  **Great models**: Llama 3.1 70B, Mixtral, Gemma
-  **Reliable**: High uptime, stable API

## Project Structure

```
kelly-scientist-bot/
├─ app.py                      # Streamlit web interface
├─ kelly_ai_scientist/
│  ├─ __init__.py
│  └─ kelly.py                 # Core LLM-powered implementation
├─ requirements.txt
├─ SETUP.md                    # Detailed setup guide
├─ LICENSE
└─ README.md
```

## Privacy & Security

 **Your API key is secure:**
- Stored only in browser session
- Never logged or saved to disk
- Not visible to anyone else
- Cleared when you close browser

 **Your conversations:**
- Stored only in session
- Can be cleared anytime
- Can be downloaded as JSON

## Fallback Mode

Don't have an API key? Kelly still works with basic template-based responses! Just run the app without entering a key.

## Design Philosophy

### Why LLM-Powered?

- **Dynamic**: Every response is unique and context-aware
- **Intelligent**: True understanding of nuanced questions
- **Creative**: Generates novel metaphors and insights
- **Still Skeptical**: System prompt ensures Kelly's personality remains

### Why Poetry?

- **Memorable**: Poetic structure makes key points stick
- **Balanced**: Forces concise expression of complex ideas
- **Engaging**: More interesting than typical chatbot responses
- **Appropriate**: The constraint mirrors AI's own constraints

## Contributing

Contributions welcome! Areas for improvement:

- Additional prompt engineering for better poems
- More model options
- Improved error handling
- Better mobile UI
- Additional features

## License

MIT License - see LICENSE file for details

## Acknowledgments

Built with:
- [Groq](https://groq.com/) for lightning-fast LLM inference
- [Streamlit](https://streamlit.io/) for the web interface
- [Llama 3.1](https://ai.meta.com/llama/) models from Meta

---

**Remember**: Kelly is skeptical by design. She questions bold claims and highlights limitations to encourage critical thinking about AI technology. If you want an AI that agrees with everything you say, Kelly is not that AI. 🤖📊🔬

**Get started in 30 seconds**: Get your [free Groq API key](https://console.groq.com) and start chatting!
