SHELL ?= /bin/zsh
VENV ?= ".venv"
VENV_ACTIVATE ?= $(VENV)/bin/activate
PROMPT ?="Who is the current president of the United States of America?"

env:
	@echo "To activate your env, run:"
	@echo 'eval "$$(make -s activate)"'

activate:
	@echo "source $(VENV_ACTIVATE)"

run:
	uv run python main.py "$(PROMPT)"

run-with-prompt:
	uv run python main.py "$(PROMPT)"

lint:
	uv run pre-commit run ruff-check

fmt format:
	uv run pre-commit run ruff-format

test-basic:
	uv run test_get_files_info.py
make test:
	uv run pytest -q

precommit: lint fmt test
	@echo "✅ ready to commit!"
