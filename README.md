# project: agent-one by [@iamserda](https://iamserda.github.io)

A crude, local-first take on Claude Code, wired into Google’s Gemini API for code-aware prompts and quick experiments.

## What it does
- Routes your prompts to Gemini for code-focused replies.
- Leaves room to grow into an editor/agent loop (file edits, refactors, notes).
- Stays small and hackable for rapid prototyping.

## Getting started
1) Install Python 3.12+ and create a virtualenv.
2) Add your Gemini key to `.env`:
    - `GEMINI_API_KEY=your-google-gemini-generated-api-key`

3) Install deps (uses `uv`; swap for pip if you prefer):
    - `uv sync`
    - `uv run python main.py`

## Next steps
- Teach the agent to read/write files and summarize diffs.
- Add prompt presets for “explain”, “review”, “refactor”.
- Wire in tests around the Gemini client and prompt formatting.
