"""
Kelly — AI Scientist Chatbot (LLM-Powered Version)

Now uses free LLM APIs to generate dynamic, context-aware poetic responses
while maintaining Kelly's skeptical, analytical, and professional tone.
"""

from dataclasses import dataclass
from typing import Optional
import os
import json

try:
    import requests
except ImportError:
    print("Please install requests: pip install requests")
    raise


@dataclass
class KellyScientist:
    """LLM-powered generator for Kelly-style poems."""
    stanzas: int = 4
    lines_per_stanza: int = 4
    api_key: Optional[str] = None
    api_provider: str = "groq"  # Options: "groq", "huggingface", "together", "openai"
    model: str = "llama-3.1-70b-versatile"  # Default Groq model
    
    def __post_init__(self):
        """Initialize API key from environment if not provided."""
        if not self.api_key:
            if self.api_provider == "groq":
                self.api_key = os.getenv("GROQ_API_KEY")
            elif self.api_provider == "huggingface":
                self.api_key = os.getenv("HUGGINGFACE_API_KEY")
            elif self.api_provider == "together":
                self.api_key = os.getenv("TOGETHER_API_KEY")
            elif self.api_provider == "openai":
                self.api_key = os.getenv("OPENAI_API_KEY")
        
        if not self.api_key:
            print(f"Warning: No API key found. Set {self.api_provider.upper()}_API_KEY environment variable.")
    
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
    
    def _call_huggingface(self, prompt: str) -> str:
        """Call Hugging Face Inference API."""
        url = f"https://api-inference.huggingface.co/models/{self.model}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        full_prompt = f"{self._get_system_prompt()}\n\nUser question: {prompt}\n\nKelly's poetic response:"
        
        response = requests.post(
            url,
            headers=headers,
            json={"inputs": full_prompt, "parameters": {"max_new_tokens": 1000, "temperature": 0.8}},
            timeout=30
        )
        response.raise_for_status()
        return response.json()[0]["generated_text"].split("Kelly's poetic response:")[-1].strip()
    
    def _call_together(self, prompt: str) -> str:
        """Call Together AI API."""
        url = "https://api.together.xyz/v1/chat/completions"
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
    
    def _call_openai(self, prompt: str) -> str:
        """Call OpenAI-compatible API."""
        url = "https://api.openai.com/v1/chat/completions"
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
        """Generate a poetic response using LLM."""
        if not self.api_key:
            return self._fallback_response(question)
        
        # Enhance prompt with extra suggestions if provided
        prompt = f"Question: {question}"
        if extra_suggestions:
            prompt += f"\n\nPlease incorporate these suggestions: {', '.join(extra_suggestions)}"
        
        try:
            if self.api_provider == "groq":
                response = self._call_groq(prompt)
            elif self.api_provider == "huggingface":
                response = self._call_huggingface(prompt)
            elif self.api_provider == "together":
                response = self._call_together(prompt)
            elif self.api_provider == "openai":
                response = self._call_openai(prompt)
            else:
                raise ValueError(f"Unknown API provider: {self.api_provider}")
            
            return response.strip()
        
        except Exception as e:
            print(f"Error calling {self.api_provider} API: {e}")
            return self._fallback_response(question)
    
    def _fallback_response(self, question: str) -> str:
        """Fallback template-based response when API is unavailable."""
        return f"""Tell me again—how sure are we of the claims you make?

What evidence supports this view of artificial minds?
Metrics measure narrow tasks, not understanding itself.
Benchmarks capture snapshots, not the shifting world outside.
Without context and care, we mistake correlation for truth.

Data remembers the past, not the future we hope to build.
Patterns can mimic intent, yet intent is not a pattern.
Deployment reveals what controlled tests failed to predict.
Generalization is narrow when reality exceeds our training sets.

Run preregistered tests with diverse, representative data.
Add uncertainty estimates; acknowledge what models cannot know.
Monitor for drift and bias in production environments.
Build with guardrails, human oversight, and graceful failure modes.

Skepticism is not cynicism; it is care with a spine.
Let evidence be the rhythm, and humility the rhyme.

[Note: API unavailable - using fallback template. Please set your API key.]"""


def demo():
    """Demo the LLM-powered Kelly."""
    # Try to use Groq (free tier available)
    kelly = KellyScientist(api_provider="groq")
    
    question = "Can AI truly understand human emotions?"
    print(f"Question: {question}\n")
    print("Kelly's Response:")
    print(kelly.generate(question))


if __name__ == "__main__":
    demo()
