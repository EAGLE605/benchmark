# Contributing to Benchmark Tool

We welcome contributions to the Benchmark Tool! This document provides guidelines for contributing to ensure high code quality and consistency.

## Code Quality Standards

### Coding Standards

All code must adhere to the following standards:

- **PEP 8**: Python style guide compliance
- **Type Hints**: Full type annotation coverage for all functions
- **Docstrings**: Google-style docstring format for all classes and functions
- **Import Sorting**: Organized imports using isort
- **Code Formatting**: Black code formatter with 88-character line length

### Quality Tools Configuration

The project uses the following tools for quality assurance:

- **Black**: Code formatting (`line-length = 88`)
- **isort**: Import sorting (black-compatible profile)
- **flake8**: Linting and style checking
- **mypy**: Static type checking (strict mode)
- **pytest**: Testing framework with coverage reporting

## Development Workflow

### 1. Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/EAGLE605/benchmark.git
cd benchmark

# Install development dependencies
make install-dev
```

### 2. Code Quality Checks

Before submitting any changes, run all quality checks:

```bash
# Run all checks
make check

# Or run individual checks
make lint          # Linting
make format        # Code formatting
make type-check    # Type checking
make test          # Tests
```

### 3. Automated Code Audit

Use the automated code audit script to ensure compliance:

```bash
python scripts/audit_code.py
```

This script will check:
- Project structure
- Code formatting (Black)
- Import sorting (isort)
- Code quality (flake8)
- Type annotations (mypy)
- Test coverage (pytest)

### 4. Writing Tests

- Write tests for all new functionality
- Maintain or improve test coverage
- Use descriptive test names
- Follow existing test patterns
- Mock external dependencies

Example test structure:
```python
def test_feature_specific_behavior() -> None:
    """Test specific behavior with clear description."""
    # Arrange
    setup_data = create_test_data()
    
    # Act
    result = function_under_test(setup_data)
    
    # Assert
    assert result.expected_property == expected_value
```

### 5. Code Review Checklist

Before submitting a PR, ensure:

- [ ] All code follows PEP 8 standards
- [ ] Type hints are provided for all functions
- [ ] Docstrings follow Google style format
- [ ] Tests are written for new functionality
- [ ] Code audit passes all checks
- [ ] No breaking changes to existing API
- [ ] Performance implications are considered
- [ ] Error handling is appropriate

## Contribution Process

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature`
3. **Write** code following the standards above
4. **Run** code audit: `python scripts/audit_code.py`
5. **Ensure** all tests pass: `make test`
6. **Commit** changes with descriptive messages
7. **Push** to your fork
8. **Create** a Pull Request

### Commit Message Format

Use clear, descriptive commit messages:

```
feat: add new benchmarking metric for disk I/O
fix: resolve memory leak in long-running benchmarks  
docs: update API documentation for BenchmarkRunner
test: add tests for edge cases in utils module
refactor: improve performance of result aggregation
```

## Code Style Examples

### Function Documentation

```python
def benchmark_function(
    func: Callable[..., Any], 
    iterations: int = 10,
    measure_memory: bool = True
) -> BenchmarkResult:
    """Run a benchmark on the given function.
    
    Args:
        func: Function to benchmark
        iterations: Number of times to run the function
        measure_memory: Whether to track memory usage
        
    Returns:
        BenchmarkResult containing performance metrics
        
    Raises:
        ValueError: If iterations is less than 1
    """
```

### Type Annotations

```python
from typing import Dict, List, Optional, Union

# Good - explicit types
def process_results(
    results: List[BenchmarkResult],
    filters: Optional[Dict[str, Any]] = None
) -> Dict[str, Union[float, int]]:
    """Process benchmark results with optional filtering."""
```

### Error Handling

```python
def validate_input(value: int) -> None:
    """Validate input parameter.
    
    Args:
        value: Value to validate
        
    Raises:
        ValueError: If value is invalid
    """
    if value <= 0:
        raise ValueError(f"Value must be positive, got {value}")
```

## Testing Guidelines

### Test Organization

- Place tests in the `tests/` directory
- Mirror the structure of the main package
- Use descriptive test file names: `test_<module>.py`

### Test Categories

1. **Unit Tests**: Test individual functions/methods
2. **Integration Tests**: Test component interactions
3. **Performance Tests**: Verify performance characteristics

### Mock Usage

Mock external dependencies to ensure test isolation:

```python
from unittest.mock import patch

@patch("psutil.Process")
def test_cpu_measurement(mock_process):
    """Test CPU usage measurement."""
    mock_instance = mock_process.return_value
    mock_instance.cpu_percent.return_value = 25.0
    
    # Test implementation
```

## Performance Considerations

- Minimize memory allocations in hot paths
- Use appropriate data structures
- Consider time complexity of algorithms
- Profile performance-critical code
- Document performance characteristics

## Documentation

- Keep README.md up to date
- Document all public APIs
- Include usage examples
- Update CHANGELOG for significant changes
- Use clear, concise language

## Questions and Support

If you have questions about contributing:

1. Check existing [GitHub Issues](https://github.com/EAGLE605/benchmark/issues)
2. Search previous discussions
3. Create a new issue with the "question" label
4. Provide clear context and examples

Thank you for contributing to the Benchmark Tool! 🚀