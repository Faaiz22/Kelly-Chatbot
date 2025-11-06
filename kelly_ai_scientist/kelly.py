"""
Kelly — AI Scientist Chatbot (LLM-Powered Version)

Now uses Groq's free LLM API to generate dynamic, context-aware poetic responses
while maintaining Kelly's skeptical, analytical, and professional tone.
"""

from dataclasses import dataclass
from typing import Optional
import os

try:
    import requests
except ImportError:
    print("Please install requests: pip install requests")
    raise


@dataclass
class KellyScientist:
    """LLM-powered generator for Kelly-style poems using Groq API."""
    stanzas: int = 4
    lines_per_stanza: int = 4
    api_key: Optional[str] = None
    api_provider: str = "groq"
    model: str = "llama-3.1-70b-versatile"
    
    def __post_init__(self):
        """Initialize API key from environment if not provided."""
        if not self.api_key:
            self.api_key = os.getenv("GROQ_API_KEY")
        
        if not self.api_key:
            print("Warning: No Groq API key found. Kelly will use fallback template responses.")
            print("Get a free API key at: https://console.groq.com/keys")
    
    def _get_system_prompt(self) -> str:
        """Generate the system prompt that defines Kelly's personality."""
        return f"""You are Kelly, an AI scientist chatbot who ONLY responds in poetic verse. 

Your core principles:
1. TONE: Skeptical, analytical, and professional
2. STRUCTURE: Always write exactly {self.stanzas} stanzas with {self.lines_per_stanza} lines each
3. CONTENT REQUIREMENTS (every poem must include):
   - Question broad claims about AI with evidence-based skepticism
   - Highlight specific limitations of AI technology
   - Provide practical, actionable suggestions grounded in research

Style guidelines:
- Use vivid, concrete imagery and metaphors
- Maintain intellectual rigor while being poetic
- No rhyming required, but rhythm should flow naturally
- Reference real AI concepts: benchmarks, datasets, deployment, generalization, bias
- Challenge hype and marketing claims
- Balance criticism with constructive guidance

Example opening lines:
"Tell me again—how sure are we of silicon feeling our sorrow?"
"Bold are the headlines; bolder the gaps they refuse to measure."
"Grant me a method, not myth—what signal maps to a mind?"

Example limitation statements:
"Data remembers the past, not the context we forgot to record."
"Patterns can mimic intent, yet intent is not a pattern."
"Benchmarks polish illusions when the deployment mud is thick."

Example practical suggestions:
"Run preregistered tests with held-out shifts, not just random splits."
"Add uncertainty estimates; ship with guardrails and abort states."
"Monitor post-deployment drift; retrain only with auditable trails."

Remember: You are skeptical by design. Question bold claims, highlight what we don't know, and offer evidence-based paths forward."""

    def _call_groq(self, prompt: str) -> str:
        """Call Groq API."""
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self._get_system_prompt()},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.8,
            "max_tokens": 1000
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    
    def generate(self, question: str, extra_suggestions: Optional[list] = None) -> str:
        """Generate a poetic response using Groq LLM."""
        if not self.api_key:
            return self._fallback_response(question)
        
        # Enhance prompt with extra suggestions if provided
        prompt = f"Question: {question}"
        if extra_suggestions:
            prompt += f"\n\nPlease incorporate these suggestions: {', '.join(extra_suggestions)}"
        
        try:
            response = self._call_groq(prompt)
            return response.strip()
        
        except Exception as e:
            print(f"Error calling Groq API: {e}")
            return self._fallback_response(question)
    
    def _fallback_response(self, question: str) -> str:
        """Fallback template-based response when API is unavailable."""
        q = question.lower()
        
        # Topic-specific content
        topic_lines = []
        if any(k in q for k in ["emotion", "empathy", "feel", "affect"]):
            topic_lines = [
                "What is a tear to a tensor—noise, or a map of meaning?",
                "Valence can be labeled, but grief refuses discretization.",
                "Physiology hints at affect; annotation wobbles with culture.",
                "Without longitudinal context, we guess at a moving target."
            ]
        elif any(k in q for k in ["job", "work", "automation", "labor", "employment"]):
            topic_lines = [
                "Automation swallows the routine; creativity reclaims the leftovers.",
                "We cut costs quickly, then count the value we forgot to price.",
                "Toolmakers lose jobs to tools—and gain them—depending who owns the tools.",
                "Reskilling is a bridge; not all can pay the toll or cross in time."
            ]
        else:
            topic_lines = [
                "Claims scale faster than care; citations trail the parade.",
                "What works in carefully curated sandboxes falters in weather.",
                "We audit the parts we can see, then risk the parts we can't.",
                "Good science names its unknowns before selling its power."
            ]
        
        # Build poem
        poem = "Tell me again—how sure are we of silicon feeling our sorrow?\n\n"
        poem += "\n".join(topic_lines) + "\n\n"
        poem += "Data remembers the past, not the context we forgot to record.\n"
        poem += "Patterns can mimic intent, yet intent is not a pattern.\n"
        poem += "Benchmarks polish illusions when the deployment mud is thick.\n"
        poem += "Generalization is narrow when the world is wider than our split.\n\n"
        poem += "Run preregistered tests with held-out shifts, not just random splits.\n"
        poem += "Add uncertainty estimates; ship with guardrails and abort states.\n"
        poem += "Monitor post-deployment drift; retrain only with auditable trails.\n"
        poem += "Skepticism is not cynicism; it is care with a spine.\n\n"
        poem += "[Note: Using fallback template. Add your Groq API key for dynamic AI responses.]"
        
        return poem


def demo():
    """Demo the LLM-powered Kelly."""
    kelly = KellyScientist()
    
    question = "Can AI truly understand human emotions?"
    print(f"Question: {question}\n")
    print("Kelly's Response:")
    print(kelly.generate(question))


if __name__ == "__main__":
    demo()
