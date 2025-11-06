# Kelly — AI Scientist Chatbot

A lightweight, dependency-free chatbot that answers **only in poems** with a **skeptical, analytical, and professional** tone.

Every poem:
1. Questions broad claims about AI
2. Highlights limitations of AI technology
3. Offers practical, evidence-based suggestions

## Features

- 📝 **Template-based poetry generation** - deterministic and reproducible
- 🔬 **Evidence-based responses** - grounded in AI research limitations
- ⚖️ **Skeptical tone** - questions hype and marketing claims
- 🎯 **Topic-aware** - adjusts content based on question keywords
- 🎨 **Customizable structure** - configure stanzas and lines per stanza
- 🚀 **Web interface** - interactive Streamlit UI
- ✅ **Well-tested** - comprehensive unit test suite

## Quick Start

### Web Interface

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

### Command Line

```python
from kelly_ai_scientist.kelly import KellyScientist

kelly = KellyScientist()
poem = kelly.generate("Can AI understand human emotions?")
print(poem)
```

## Project Structure

```
kelly-scientist-bot/
├─ app.py                      # Streamlit web interface
├─ kelly_ai_scientist/
│  ├─ __init__.py
│  └─ kelly.py                 # Core implementation
├─ tests/
│  └─ test_kelly.py           # Unit tests
├─ requirements.txt
├─ LICENSE
└─ README.md
```

## How It Works

Kelly uses a **template-based system** (not an LLM) to ensure consistent, evidence-based responses:

1. **Question Analysis**: Extracts keywords to identify topic (emotions, jobs, creativity, etc.)
2. **Content Selection**: Chooses relevant content blocks from curated pools:
   - Skeptical openers
   - Topic-specific analysis
   - AI limitations
   - Practical suggestions
   - Professional closers
3. **Poem Assembly**: Combines blocks into structured stanzas with proper formatting

### Example

**Input:** "Can AI truly understand human emotions?"

**Output:**
```
Tell me again—how sure are we of silicon feeling our sorrow?

What is a tear to a tensor—noise, or a map of meaning?
Valence can be labeled, but grief refuses discretization.
Physiology hints at affect; annotation wobbles with culture.
Without longitudinal context, we guess at a moving target.

Data remembers the past, not the context we forgot to record.
Patterns can mimic intent, yet intent is not a pattern.
Benchmarks polish illusions when the deployment mud is thick.
Generalization is narrow when the world is wider than our split.

...
```

## Customization

```python
# Change poem structure
kelly = KellyScientist(stanzas=3, lines_per_stanza=5)

# Add custom suggestions
poem = kelly.generate(
    "How do we test AI?",
    extra_suggestions=["Always validate with real-world data."]
)
```

## Design Philosophy

### Why Template-Based?

- **Consistency**: Every response includes skepticism, limitations, and practical advice
- **Transparency**: No black-box LLM - all content is curated and auditable
- **Reliability**: Deterministic output prevents hallucination or inappropriate content
- **Educational**: Designed to encourage critical thinking about AI claims

### Why Poetry?

- **Memorable**: Poetic structure makes key points stick
- **Balanced**: Forces concise expression of complex ideas
- **Engaging**: More interesting than typical chatbot responses
- **Appropriate**: The constraint mirrors AI's own constraints

## Topics Covered

- 🧠 AI Emotions & Empathy
- 💼 Job Automation & Labor
- 🎨 Creativity & Originality  
- 🤔 Consciousness & Sentience
- ⚖️ Bias & Fairness
- 🛡️ AI Safety & Risks
- 🧩 Intelligence & Reasoning
- 🔮 Future Predictions
- 📚 Machine Learning
- 🚧 AI Limitations

## Testing

Run the test suite:

```bash
python -m pytest tests/
# or
python tests/test_kelly.py
```

Tests cover:
- Poem structure and formatting
- Topic detection and content selection
- Deterministic output
- Response quality (skepticism, limitations, practical advice)
- Edge cases (empty questions, long questions, etc.)

## Development

### Adding New Topics

1. Add keywords to `_topic_specific_blocks()` in `kelly.py`
2. Add corresponding content blocks
3. Add tests in `test_kelly.py`

### Adding New Content

Edit the content pools in `kelly.py`:
- `SKEPTICAL_OPENERS`: Opening lines that question claims
- `LIMITATIONS_LINES`: Statements about AI limitations
- `PRACTICAL_SUGGESTIONS`: Evidence-based advice
- `CLOSERS`: Concluding statements

## Limitations

Kelly herself would want you to know:

- ❌ **Not an LLM**: Uses templates, not generative AI
- ❌ **Limited knowledge**: Content is curated, not comprehensive
- ❌ **Topic-dependent**: Best for AI-related questions
- ❌ **Fixed structure**: Always produces poems in the same format
- ✅ **By design**: These limitations ensure reliability and consistency

## Contributing

Contributions welcome! Areas for improvement:

- More topic-specific content blocks
- Better keyword extraction
- Additional poem styles
- Improved web interface
- More comprehensive tests

## License

MIT License - see LICENSE file for details

## Acknowledgments

Built with:
- [Streamlit](https://streamlit.io/) for the web interface
- Python's `dataclasses` for clean configuration
- No external AI/ML dependencies (intentionally!)

---

**Remember**: Kelly is skeptical by design. She questions bold claims and highlights limitations to encourage critical thinking about AI technology. If you want an AI that agrees with everything you say, Kelly is not that AI. 🤖📊🔬
