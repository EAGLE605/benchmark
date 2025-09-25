# Benchmark Tool

A comprehensive Python benchmarking tool for performance testing and measurement with built-in code quality standards and syntax compliance.

## Features

- 🚀 **High-Performance Benchmarking**: Accurate timing and resource measurement
- 📊 **Comprehensive Metrics**: Execution time, memory usage, and CPU utilization
- 🔧 **Flexible Configuration**: Customizable iterations, setup/teardown functions
- 📈 **Rich Reporting**: Formatted tables with sorting and filtering options
- 🎯 **CLI Interface**: Easy-to-use command-line interface
- ✅ **Code Quality**: Built-in linting, formatting, and type checking
- 🧪 **Test Coverage**: Comprehensive test suite with coverage reporting

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/EAGLE605/benchmark.git
cd benchmark

# Install in development mode
pip install -e .[dev]
```

### Production Install

```bash
pip install -e .
```

## Quick Start

### Command Line Usage

```bash
# Run example benchmarks
benchmark

# Customize iterations and sorting
benchmark --iterations 20 --sort-by memory_usage --verbose

# Disable memory/CPU measurement
benchmark --no-memory --no-cpu
```

### Python API Usage

```python
from benchmark import Benchmark, BenchmarkRunner

# Create a simple benchmark
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Set up benchmark
benchmark = Benchmark(
    name="Fibonacci Calculation",
    func=fibonacci,
    iterations=10,
    measure_memory=True,
    measure_cpu=True
)

# Run benchmark
result = benchmark.run(25)
print(f"Average time: {result.execution_time:.4f}s")

# Use benchmark runner for multiple tests
runner = BenchmarkRunner()
runner.add_benchmark(benchmark)
results = runner.run_all()
print(runner.generate_report())
```

## Code Quality Standards

This project follows strict coding standards and syntax compliance:

### Coding Standards

- **PEP 8**: Python style guide compliance
- **Type Hints**: Full type annotation coverage
- **Docstrings**: Google-style docstring format
- **Import Sorting**: Organized imports with isort
- **Code Formatting**: Black code formatter (88-character line length)

### Quality Tools

- **Black**: Code formatting (`black benchmark tests`)
- **isort**: Import sorting (`isort benchmark tests`)
- **flake8**: Linting and style checking (`flake8 benchmark tests`)
- **mypy**: Static type checking (`mypy benchmark`)
- **pytest**: Testing framework with coverage (`pytest tests/ --cov=benchmark`)

### Running Code Audit

```bash
# Run complete code audit
python scripts/audit_code.py

# Run individual checks
make lint          # Linting checks
make format        # Code formatting
make type-check    # Type checking
make test          # Run tests
make check         # All checks combined
```

## Development

### Setup Development Environment

```bash
# Install development dependencies
make install-dev

# Run all setup and checks
make all
```

### Available Make Targets

```bash
make help          # Show all available targets
make install       # Install production dependencies
make install-dev   # Install development dependencies
make lint          # Run linting checks
make format        # Format code with black and isort
make type-check    # Run type checking with mypy
make test          # Run tests
make test-coverage # Run tests with coverage
make clean         # Clean build artifacts
make check         # Run all checks (lint, type-check, test)
make ci-check      # Run CI checks with coverage
```

### Project Structure

```
benchmark/
├── benchmark/           # Main package
│   ├── __init__.py     # Package exports
│   ├── core.py         # Core benchmarking classes
│   ├── runner.py       # Benchmark runner
│   ├── utils.py        # Utility functions
│   └── cli.py          # Command-line interface
├── tests/              # Test suite
│   ├── test_core.py    # Core functionality tests
│   ├── test_runner.py  # Runner tests
│   └── test_utils.py   # Utility tests
├── scripts/            # Development scripts
│   └── audit_code.py   # Code audit script
├── pyproject.toml      # Project configuration
├── .flake8            # Flake8 configuration
├── .gitignore         # Git ignore rules
├── Makefile           # Development automation
└── README.md          # This file
```

## Configuration Files

### pyproject.toml

Complete project configuration including:
- Build system setup
- Dependencies (production and development)
- Tool configuration (black, isort, mypy, pytest)
- Code coverage settings

### .flake8

Linting configuration:
- Line length: 88 characters (consistent with black)
- Ignored error codes for compatibility
- Per-file ignore rules for specific cases

## Testing

Run the complete test suite:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=benchmark --cov-report=html

# Run specific test file
pytest tests/test_core.py -v
```

## Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make changes following coding standards**
4. **Run code audit**: `python scripts/audit_code.py`
5. **Ensure all tests pass**: `make check`
6. **Commit changes**: `git commit -m "Description"`
7. **Push to branch**: `git push origin feature-name`
8. **Create Pull Request**

### Code Review Checklist

- [ ] All code follows PEP 8 standards
- [ ] Type hints are provided for all functions
- [ ] Docstrings follow Google style format
- [ ] Tests are written for new functionality
- [ ] Code audit passes all checks
- [ ] No breaking changes to existing API

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions, issues, or contributions, please:

1. Check existing [GitHub Issues](https://github.com/EAGLE605/benchmark/issues)
2. Create a new issue with detailed description
3. Follow the contributing guidelines above

---

**Made with ❤️ for performance testing and code quality**
