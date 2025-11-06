# Kelly AI Scientist - Quick Setup Guide

## Get Your Free Groq API Key (30 seconds)

1. **Visit Groq Console**: https://console.groq.com
2. **Sign Up**: Create a free account (no credit card required)
3. **Get API Key**: 
   - Click on "API Keys" in the left menu
   - Click "Create API Key"
   - Copy your key (starts with `gsk_`)

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Using Kelly

### Method 1: Through Streamlit Interface (Recommended)

1. Run `streamlit run app.py`
2. In the sidebar, paste your Groq API key in the "API Key" field
3. Start chatting with Kelly!

**Your API key is:**
- ✅ Stored only in your browser session
- ✅ Never logged or saved to disk
- ✅ Completely private and secure

### Method 2: Through Environment Variable

```bash
# Set environment variable
export GROQ_API_KEY="your-api-key-here"

# Run the app
streamlit run app.py
```

### Method 3: In Python Code

```python
from kelly_ai_scientist.kelly import KellyScientist

# Option A: Pass API key directly
kelly = KellyScientist(api_key="your-groq-key-here")

# Option B: Use environment variable
# (set GROQ_API_KEY in your environment)
kelly = KellyScientist()

# Generate a poem
poem = kelly.generate("Can AI understand emotions?")
print(poem)
```

## Groq Models Available

Choose from these models in the Streamlit interface:

| Model | Description | Speed |
|-------|-------------|-------|
| **llama-3.1-70b-versatile** | Most intelligent, best quality | Medium |
| **llama-3.1-8b-instant** | Fast responses, good quality | Very Fast |
| **mixtral-8x7b-32768** | Large context window | Medium |
| **gemma2-9b-it** | Efficient, good quality | Fast |

**Recommendation**: Start with `llama-3.1-70b-versatile` for best results.

## Features

✅ **Free & Fast**: Groq offers ~14,400 free requests/day  
✅ **No Template**: True AI-generated, context-aware poems  
✅ **Maintains Voice**: Kelly's skeptical, analytical personality  
✅ **Secure**: API keys stored only in your session  
✅ **Fallback Mode**: Works without API key (basic templates)  

## Troubleshooting

### "No API key found" warning
- **Solution**: Enter your API key in the sidebar of the Streamlit app
- Or set `GROQ_API_KEY` environment variable

### API request fails
- **Check**: Your API key is correct (starts with `gsk_`)
- **Check**: You have internet connection
- **Check**: You haven't exceeded rate limits (~14,400 requests/day)
- **Solution**: Try again or use fallback mode

### Slow responses
- **Try**: Switch to `llama-3.1-8b-instant` model (faster)
- **Note**: First request might be slower (cold start)

## Rate Limits

- **Free Tier**: ~14,400 requests per day
- **Rate**: ~30 requests per minute
- **More than enough** for personal use!

## Example Questions

Try asking Kelly about:
- "Can AI understand human emotions?"
- "Will AI replace all jobs?"
- "Is AI truly creative?"
- "Can machines become conscious?"
- "How do we address AI bias?"
- "What are the limitations of AI?"
- "How intelligent is AI really?"

## Privacy & Security

🔒 **Your API key is secure:**
- Stored only in browser session (not on disk)
- Never logged or transmitted except to Groq
- Cleared when you close the browser
- Not visible to anyone else

🔒 **Your conversations:**
- Stored only in browser session
- Can be cleared anytime with "Clear Chat History"
- Can be downloaded as JSON for your records

## Need More Help?

- **Groq Documentation**: https://console.groq.com/docs
- **Groq API Keys**: https://console.groq.com/keys
- **Rate Limits**: https://console.groq.com/docs/rate-limits

## What's Different from Original Kelly?

| Feature | Original | New (LLM) |
|---------|----------|-----------|
| Response Type | Fixed templates | AI-generated |
| Context Awareness | Limited | Full understanding |
| Creativity | Same poems | Unique every time |
| Topics | 10-12 predefined | Unlimited |
| Setup | None needed | API key needed |
| Cost | Free | Free (Groq) |

**The new Kelly is smarter, more creative, and truly conversational!**

---

**Happy chatting with Kelly! 🤖📊🔬**
