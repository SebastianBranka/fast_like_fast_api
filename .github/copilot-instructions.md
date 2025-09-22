# Copilot Instructions for FastLikeFastAPI

## Project Overview
This is a minimal Python project with a focus on simple scripts and Jupyter notebooks. The codebase currently contains:
- `hello.py`: A basic script for testing environment setup.
- `programs.ipynb`: Example notebook with a simple function and print statements.
- `requirements.txt`: Lists all dependencies, including development tools (black, pytest, poetry) and runtime packages.

## Key Workflows
- **Run scripts:** Use `python hello.py` for basic script execution.
- **Jupyter Notebooks:** Edit and run cells in `programs.ipynb` for interactive development.
- **Dependency management:** Install dependencies with `pip install -r requirements.txt`. Poetry is also available for advanced dependency management (`poetry install`).
- **Testing:** Use `pytest` for running tests (no test files present yet, but pytest is installed).
- **Formatting:** Use `black` for code formatting (`black .`).

## Conventions & Patterns
- Keep scripts simple and self-contained.
- Use print statements for output and debugging.
- Notebook cells should be executable independently.
- All dependencies should be listed in `requirements.txt`.
- Prefer Poetry for reproducible environments if adding new dependencies.

## External Dependencies
- See `requirements.txt` for all packages. Notable tools: `black`, `pytest`, `poetry`.
- No web frameworks or FastAPI present, despite the project name.

## Examples
- Script: `hello.py` prints "hello".
- Notebook: `programs.ipynb` defines and calls `paid_promotion()`.

## Recommendations for AI Agents
- When adding new scripts, follow the style of `hello.py` (simple, direct).
- For notebooks, ensure new cells are clear and runnable independently.
- Update `requirements.txt` when adding new dependencies.
- Use Poetry for dependency management if project complexity increases.
- If introducing tests, place them in a `tests/` directory and use `pytest`.

## Directory Reference
- `/hello.py`: Example script
- `/programs.ipynb`: Example notebook
- `/requirements.txt`: Dependency list
- `/.github/copilot-instructions.md`: This guide

---

If any conventions or workflows are unclear or missing, please provide feedback to improve these instructions.
