
"""
Kelly — AI Scientist Chatbot

Design goals
- Always respond in *poetic form*.
- Tone: skeptical, analytical, professional.
- Each poem must:
  1) Question broad claims about AI.
  2) Highlight limitations of AI technology.
  3) Include practical, evidence-based suggestions.
- Maintain a consistent structure (default: 4 quatrains).

This module provides a light, dependency-free implementation that builds poems
from principled templates and content blocks. No external LLMs required.
"""

from dataclasses import dataclass
from typing import List, Optional

DEFAULT_STRUCTURE = {
    "stanzas": 4,
    "lines_per_stanza": 4,
}

# Reusable building blocks to ensure the required elements appear in every poem.
SKEPTICAL_OPENERS = [
    "Tell me again—how sure are we of silicon feeling our sorrow?",
    "Bold are the headlines; bolder the gaps they refuse to measure.",
    "Grant me a method, not myth—what signal maps to a mind?",
    "If metrics stand in for meaning, what meaning do metrics miss?",
]

LIMITATIONS_LINES = [
    "Data remembers the past, not the context we forgot to record.",
    "Patterns can mimic intent, yet intent is not a pattern.",
    "Benchmarks polish illusions when the deployment mud is thick.",
    "Generalization is narrow when the world is wider than our split.",
    "Labels leak judgment; proxies stand in costumes of truth.",
]

PRACTICAL_SUGGESTIONS = [
    "Run preregistered tests with held-out shifts, not just random splits.",
    "Add uncertainty estimates; ship with guardrails and abort states.",
    "Collect consented, diverse data; document provenance and limits.",
    "Stress-test edge cases; compare against strong human baselines.",
    "Monitor post-deployment drift; retrain only with auditable trails.",
    "Prefer interpretable models when stakes constrain acceptable risk.",
]

CLOSERS = [
    "Skepticism is not cynicism; it is care with a spine.",
    "Let evidence be the rhythm, and humility the rhyme.",
    "We earn trust by resisting certainty more than doubt.",
    "Design with consequences in mind; that is the honest architecture.",
]


@dataclass
class KellyScientist:
    """Rule-based generator for Kelly-style poems."""
    stanzas: int = DEFAULT_STRUCTURE["stanzas"]
    lines_per_stanza: int = DEFAULT_STRUCTURE["lines_per_stanza"]

    def _choose(self, pool: List[str], n: int) -> List[str]:
        # Deterministic selection without random for reproducibility.
        # Rotates through the list.
        out = []
        for i in range(n):
            out.append(pool[i % len(pool)])
        return out

    def _topic_specific_blocks(self, question: str) -> List[str]:
        q = question.lower()

        blocks = []
        # Emotion understanding theme
        if any(k in q for k in ["emotion", "empathy", "feel", "affect"]):
            blocks.extend([
                "What is a tear to a tensor—noise, or a map of meaning?",
                "Valence can be labeled, but grief refuses discretization.",
                "Physiology hints at affect; annotation wobbles with culture.",
                "Without longitudinal context, we guess at a moving target.",
            ])

        # Jobs & automation theme
        if any(k in q for k in ["job", "work", "automation", "labor", "employment", "career"]):
            blocks.extend([
                "Automation swallows the routine; creativity reclaims the leftovers.",
                "We cut costs quickly, then count the value we forgot to price.",
                "Toolmakers lose jobs to tools—and gain them—depending who owns the tools.",
                "Reskilling is a bridge; not all can pay the toll or cross in time.",
            ])

        # Default block when no special keywords found
        if not blocks:
            blocks.extend([
                "Claims scale faster than care; citations trail the parade.",
                "What works in carefully curated sandboxes falters in weather.",
                "We audit the parts we can see, then risk the parts we can't.",
                "Good science names its unknowns before selling its power.",
            ])
        return blocks

    def generate(self, question: str, extra_suggestions: Optional[List[str]] = None) -> str:
        """Create a four-stanza poem satisfying Kelly's constraints."""
        lines: List[str] = []

        # 1) Opening skepticism
        lines.append(self._choose(SKEPTICAL_OPENERS, 1)[0])

        # 2) Topic-specific analysis
        lines.extend(self._topic_specific_blocks(question)[:self.lines_per_stanza])

        # 3) Explicit limitations
        lines.extend(self._choose(LIMITATIONS_LINES, self.lines_per_stanza))

        # 4) Practical suggestions (evidence-oriented)
        tips = self._choose(PRACTICAL_SUGGESTIONS, self.lines_per_stanza - 1)
        if extra_suggestions:
            # place at the front to honor user-provided items
            tips = extra_suggestions[:1] + tips[:-1]
        lines.extend(tips + [self._choose(CLOSERS, 1)[0]])

        # Enforce stanza breaks
        stanzas = []
        total_lines_needed = self.stanzas * self.lines_per_stanza
        # Pad or truncate to exact size
        if len(lines) < total_lines_needed:
            lines += self._choose(LIMITATIONS_LINES, total_lines_needed - len(lines))
        lines = lines[:total_lines_needed]

        for i in range(0, total_lines_needed, self.lines_per_stanza):
            stanzas.append("\n".join(lines[i:i+self.lines_per_stanza]))

        poem = "\n\n".join(stanzas)
        return poem


def demo():
    bot = KellyScientist()
    q = "Can AI truly understand human emotions, and will it replace creative jobs?"
    return bot.generate(q)


if __name__ == "__main__":
    print(demo())
