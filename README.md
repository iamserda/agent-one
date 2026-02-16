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

## Makefile recipes

### `make env`
Prints the shell command to activate the virtual environment.

### `make activate`
Prints the `source` command for activating the virtual environment.

### `make run-with-prompt`
Runs `main.py` with the prompt defined by `PROMPT`.

### `make lint`
Runs the Ruff lint check via pre-commit.

### `make fmt` / `make format`
Formats code via Ruff format through pre-commit.

### `make precommit`
Runs `lint`, `fmt`, and `test` in sequence.

## Next steps
- Teach the agent to read/write files and summarize diffs.
- Add prompt presets for “explain”, “review”, “refactor”.
- Wire in tests around the Gemini client and prompt formatting.
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
Created by [@iamserda](https://iamserda.github.io) - [GitHub](https://github.com/iamserda)

## Acknowledgments
- Powered by [Google Gemini API](https://ai.google.dev/) for code-aware responses
- Project scaffolding with [uv](https://docs.astral.sh/uv/) and [Ruff](https://docs.astral.sh/ruff/)
