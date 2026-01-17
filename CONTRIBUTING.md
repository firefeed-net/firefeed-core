# Contributing to FireFeed Core

Thank you for your interest in contributing to FireFeed Core! This document provides guidelines for contributing to the project.

## 🚀 Quick Start

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/your-username/firefeed-core.git
   cd firefeed-core
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Run tests to verify setup**
   ```bash
   pytest
   ```

### Code Style

We use several tools to maintain code quality:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

Run all checks:
```bash
# Format code
black firefeed_core/ tests/

# Sort imports
isort firefeed_core/ tests/

# Lint code
flake8 firefeed_core/ tests/

# Type checking
mypy firefeed_core/

# Run all checks (recommended)
pre-commit run --all-files
```

### Testing

We use pytest for testing. All new features should include tests.

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=firefeed_core --cov-report=html

# Run specific test file
pytest tests/test_api_client.py

# Run specific test
pytest tests/test_api_client.py::TestAPIClient::test_client_initialization
```

### Pre-commit Hooks

We use pre-commit to automatically run checks before commits:

```bash
# Install pre-commit hooks
pre-commit install

# Run pre-commit on all files
pre-commit run --all-files
```

## 📝 Development Guidelines

### Branch Naming

- Use descriptive branch names
- Use kebab-case: `feature/add-circuit-breaker`
- Prefix with type: `feature/`, `fix/`, `docs/`, `refactor/`

### Commit Messages

Use conventional commit format:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Examples:
- `feat(api-client): add circuit breaker pattern`
- `fix(auth): resolve JWT token validation issue`
- `docs: update API client usage examples`
- `refactor: extract common exception handling`

### Pull Requests

1. Create a feature branch from `develop`
2. Make your changes with tests
3. Ensure all checks pass
4. Create a pull request with:
   - Clear title following conventional commits
   - Description of changes and motivation
   - Screenshots if applicable
   - Related issue number if applicable

## 🏗️ Architecture Guidelines

### API-First Design

- All inter-service communication must go through HTTP APIs
- No direct database access between services
- Use JWT tokens for authentication
- Implement proper error handling

### Error Handling

- Use the provided exception hierarchy
- Always provide meaningful error messages
- Include relevant context in exception details
- Log errors appropriately

### Security

- Never commit secrets or tokens
- Use environment variables for configuration
- Validate all inputs
- Implement proper authentication and authorization

### Testing

- Write tests for all new functionality
- Use pytest fixtures for common test setup
- Mock external dependencies
- Test error conditions

## 📦 Package Development

### Adding New Features

1. **Create an issue** describing the feature
2. **Discuss the design** in the issue
3. **Implement the feature** with tests
4. **Update documentation**
5. **Submit a pull request**

### Adding Dependencies

1. Add to `pyproject.toml` in the appropriate section
2. Update `README.md` if it's a user-facing dependency
3. Consider backward compatibility
4. Update tests if needed

### Breaking Changes

1. **Major version bump** required
2. **Detailed migration guide** in PR description
3. **Deprecation warnings** for one minor version before removal
4. **Update documentation** with migration steps

## 🐛 Bug Reports

### Before Reporting a Bug

1. Check if the issue exists in the latest version
2. Search existing issues
3. Check the documentation

### How to Report

Create an issue with:

1. **Clear title** describing the problem
2. **Environment details** (Python version, OS, etc.)
3. **Steps to reproduce**
4. **Expected vs actual behavior**
5. **Error messages and stack traces**
6. **Minimal code example** if applicable

## 📖 Documentation

### Code Documentation

- Use docstrings for all public functions and classes
- Follow Google or NumPy docstring style
- Document parameters, returns, and exceptions

### README Updates

- Update examples when adding new features
- Keep configuration examples current
- Document breaking changes

### API Documentation

- Document all public APIs
- Include usage examples
- Document authentication requirements

## 🚀 Release Process

### Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR.MINOR.PATCH**
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)

### Release Checklist

1. **Update version** in `pyproject.toml`
2. **Update CHANGELOG.md**
3. **Run full test suite**
4. **Build and test package**
5. **Create GitHub release**
6. **Publish to PyPI** (automated by GitHub Actions)

### Pre-release Testing

```bash
# Test installation
pip install dist/firefeed_core-*.tar.gz
python -c "import firefeed_core; print('Import successful')"

# Test basic functionality
python -c "
from firefeed_core import APIClient
print('APIClient import successful')
"
```

## 🤝 Code of Conduct

Please follow these guidelines:

- Be respectful and inclusive
- Provide constructive feedback
- Help others when possible
- Follow security best practices
- Keep discussions on topic

## 📞 Getting Help

- **Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Documentation**: For usage guides and API reference

## 🙏 Thank You

Your contributions help make FireFeed Core better for everyone. We appreciate your time and effort!

---

**Note**: This document is a living document and may be updated as the project evolves.