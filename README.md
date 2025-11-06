
# Kelly — AI Scientist Chatbot

A lightweight, dependency-free chatbot that answers **only in poems** with a **skeptical, analytical, and professional** tone.
Every poem:
1. Questions broad claims about AI
2. Highlights limitations of AI technology
3. Offers practical, evidence-based suggestions

## Quick Start

```bash
python app.py "Can AI understand human emotions, and what about jobs?"
```

## Colab: Create a ZIP ready for GitHub

Run these **single-cell** steps in Google Colab to create and download `kelly-scientist-bot.zip`:

```python
# 1) Clone/assemble project structure (or copy your local files into /content/kelly-scientist-bot)
import os, pathlib, zipfile, shutil

project = "/content/kelly-scientist-bot"
if os.path.exists(project):
    shutil.rmtree(project)
shutil.copytree("/content/kelly-scientist-bot", project, dirs_exist_ok=True)  # adjust if needed

# 2) Zip the folder
zip_path = "/content/kelly-scientist-bot.zip"
def make_zip(src_dir, zip_file):
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(src_dir):
            for f in files:
                full = os.path.join(root, f)
                rel = os.path.relpath(full, src_dir)
                zf.write(full, rel)

make_zip(project, zip_path)
print("Created:", zip_path)

# 3) (Optional) Upload to GitHub using the web UI
# - Go to GitHub ➜ New repository ➜ 'Add file' ➜ 'Upload files' ➜ Drag & drop the ZIP ➜ Commit.
```

### Colab one-liner (zip any folder)
```python
import os, zipfile
def zipdir(src, dst_zip):
    with zipfile.ZipFile(dst_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(src):
            for f in files:
                p = os.path.join(root, f)
                zf.write(p, os.path.relpath(p, src))
zipdir("/content/kelly-scientist-bot", "/content/kelly-scientist-bot.zip")
```

## Structure
```
kelly-scientist-bot/
├─ app.py
├─ kelly_ai_scientist/
│  ├─ __init__.py
│  └─ kelly.py
├─ tests/
│  └─ test_kelly.py
├─ requirements.txt
├─ LICENSE
└─ README.md
```

## Design notes
- Deterministic, template-based generation to keep outputs consistent.
- Four quatrains by default; easy to change via `KellyScientist(stanzas=?, lines_per_stanza=?)`.
- Ensures inclusion of skepticism, limitations, and practical tips.
- No external dependencies.

## License
MIT
