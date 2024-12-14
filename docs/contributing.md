# Contributing Guide

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/HaiyangLi/lion-service.git
cd lion-service
```

2. Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Install development dependencies:
```bash
uv pip install -e ".[dev]"
```

## Development Workflow

1. Create a feature branch:
```bash
git checkout -b feature/your-feature
```

2. Make changes and run tests:
```bash
pytest --asyncio-mode=auto
```

3. Format code:
```bash
black .
isort .
```

## Code Style

- Use [black](https://github.com/psf/black) for formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Follow PEP 8 guidelines
- Add docstrings for public functions and classes

## Testing

- Write tests for new features
- Maintain test coverage
- Use pytest fixtures for common test setups
- Test async functions with pytest-asyncio

## Pull Request Process

1. Update documentation for new features
2. Add tests for new functionality
3. Ensure CI passes
4. Request review from maintainers

## Release Process

1. Update version in:
   - pyproject.toml
   - lion_service/version.py

2. Create release notes
3. Tag release in git
4. CI will automatically publish to PyPI

## Project Structure

```
lion_service/
├── __init__.py          # Package exports
├── imodel.py            # Main interface
├── service.py           # Base service class
├── rate_limiter.py      # Rate limiting
├── token_calculator.py  # Token counting
└── service_util.py      # Utilities
