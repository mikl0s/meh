# Developer Guidelines

1. Always use the virtual environment (`venv`) direct path (`venv/bin/*`) in all calls to Python tools (e.g., `python`, `pip`, `pytest`, `black`, `mypy`, `flake8`).
2. Run `pytest` with both `--verbose` and `--cov` to ensure comprehensive testing and coverage reporting.
3. Use `black` for code formatting to maintain consistency across the codebase.
4. Use `flake8` for linting to catch syntax errors, style issues, and potential bugs.
5. Type check your code with `mypy` to ensure type safety.
6. Write meaningful commit messages that accurately describe the changes made.
7. Follow the existing code style and conventions in the project.
8. Keep functions and methods small and focused on a single responsibility.
9. Write unit tests for all new functionality and changes.
10. Refactor code when necessary to improve readability and maintainability.
11. Avoid hardcoding values; use configuration files or environment variables where appropriate.
12. Document all public methods and classes with docstrings.
13. Use `logging` instead of print statements for debugging and information messages.
14. Keep dependencies updated, and avoid using deprecated packages.
15. Use `.gitignore` to keep sensitive or unnecessary files out of the repository.
16. Perform code reviews before merging any pull requests to ensure quality and share knowledge.
17. Use feature branches for development and merge into the main branch via pull requests.
18. Avoid committing code with failing tests or linting errors.
19. Continuously improve the test coverage to keep it at a reasonable level.
20. Use descriptive variable and function names that clearly indicate their purpose.
