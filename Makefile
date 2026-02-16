SHELL ?= /bin/zsh
VENV ?= ".venv"
PROMPT ?="Who is the current president of the United States of America?"

runp:
	uv run python main.py "$(PROMPT)"

prompt:
	uv run python main.py "$(PROMPT)"

lint:
	uv run pre-commit run ruff-check

fmt format:
	uv run pre-commit run ruff-format

precommit: lint fmt
	@echo $("ready to commit!")
