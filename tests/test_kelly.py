
from kelly_ai_scientist.kelly import KellyScientist

def test_structure():
    bot = KellyScientist()
    poem = bot.generate("Test question")
    stanzas = poem.strip().split("\n\n")
    assert len(stanzas) == bot.stanzas
    for s in stanzas:
        assert len(s.splitlines()) == bot.lines_per_stanza

def test_content_requirements():
    bot = KellyScientist()
    poem = bot.generate("Do emotions matter?")
    # Must contain skepticism and practical hints markers
    assert any(keyword in poem.lower() for keyword in ["uncertainty", "guardrails", "monitor"] + ["skepticism"])
