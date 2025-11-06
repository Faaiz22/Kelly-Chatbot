
#!/usr/bin/env python3
"""
CLI demo for Kelly — AI Scientist Chatbot.

Usage:
    python app.py "Your question about AI"
"""
import sys
from kelly_ai_scientist.kelly import KellyScientist

def main():
    if len(sys.argv) < 2:
        print("Please provide a question as a command-line argument.")
        sys.exit(1)
    question = sys.argv[1]
    bot = KellyScientist()
    poem = bot.generate(question)
    print(poem)

if __name__ == "__main__":
    main()
