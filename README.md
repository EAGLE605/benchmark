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
# Benchmark

[![CI Pipeline](https://github.com/EAGLE605/benchmark/workflows/CI%20Pipeline/badge.svg)](https://github.com/EAGLE605/benchmark/actions)
[![codecov](https://codecov.io/gh/EAGLE605/benchmark/branch/main/graph/badge.svg)](https://codecov.io/gh/EAGLE605/benchmark)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modern, well-tested Python benchmarking tool for measuring and comparing product performance with comprehensive analysis and reporting capabilities.

## Features

- 🚀 **Clean, Typed API**: Modern Python with type hints and clear interfaces
- 📊 **Statistical Analysis**: Comprehensive performance analysis with ratios and insights
- 🧪 **Well Tested**: 80%+ test coverage with comprehensive unit tests
- 🔍 **Code Quality**: Automated linting, formatting, and type checking
- 📈 **Multiple Output Formats**: Save results to JSON, CSV, or console
- 🖥️ **CLI Interface**: Easy-to-use command-line tool
- ⚡ **CI/CD Ready**: GitHub Actions workflow for automated testing
- 📋 **Audit Script**: One-command code quality validation

## Quick Start

### Installation

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
# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Basic Usage

#### As a Python Module

```python
from benchmark.bench import measure_products, analyze_results

# Benchmark multiple products
results = measure_products(['ProductA', 'ProductB', 'ProductC'], iterations=100)
print(results)
# {'ProductA': 0.001234, 'ProductB': 0.001456, 'ProductC': 0.001123}

# Analyze the results
analysis = analyze_results(results)
print(f"Fastest: {analysis['fastest_product']} ({analysis['fastest_time']:.6f}s)")
print(f"Performance ratio: {analysis['performance_ratio']:.2f}x")
```

#### Using the CLI

```bash
# Basic benchmark with default products
python -m benchmark.cli

# Custom products with more iterations
python -m benchmark.cli -p ProductA ProductB ProductC -i 500

# Save results to files with verbose output
python -m benchmark.cli --json --csv --verbose

# Custom output directory
python -m benchmark.cli --output-dir ./my_results --json
```

#### CLI Options

```
usage: python -m benchmark.cli [-h] [-p PRODUCTS [PRODUCTS ...]] [-i ITERATIONS]
                               [--output-dir OUTPUT_DIR] [--json] [--csv] [-v] [--version]

options:
  -h, --help            show this help message and exit
  -p, --products        List of product names to benchmark
  -i, --iterations      Number of iterations per product (default: 100)
  --output-dir          Output directory for results (default: benchmark_results)
  --json               Save results to JSON format
  --csv                Save results to CSV format
  -v, --verbose        Enable verbose output
  --version            show program's version number and exit
```

## API Reference

### Core Functions

#### `measure_work(work: Callable[[], None]) -> float`

Measure the execution time of a single work function.

**Parameters:**
- `work`: A callable that takes no arguments and returns None

**Returns:**
- Elapsed time in seconds as a float

**Example:**
```python
def my_work():
    time.sleep(0.001)

elapsed = measure_work(my_work)
```

#### `measure_products(products: Iterable[str], iterations: int = 1000) -> Dict[str, float]`

Benchmark multiple products with statistical analysis.

**Parameters:**
- `products`: An iterable of product identifiers to benchmark
- `iterations`: Number of iterations to run for each product (default: 1000)

**Returns:**
- Dictionary mapping product names to average execution times

#### `analyze_results(results: Dict[str, float]) -> Dict[str, Any]`

Analyze benchmark results and provide insights.

**Parameters:**
- `results`: Dictionary of product names to execution times

**Returns:**
- Dictionary with analysis including fastest, slowest, ratios, and statistics

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=benchmark --cov-report=term-missing

# Run specific test file
pytest tests/test_bench.py -v
```

### Code Quality

```bash
# Run the audit script (linting + testing)
python scripts/audit.py

# Run with additional checks
python scripts/audit.py --with-mypy --with-coverage

# Individual tools
flake8 benchmark/ tests/ scripts/
mypy benchmark/
black benchmark/ tests/ scripts/
isort benchmark/ tests/ scripts/
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
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI pipeline
├── benchmark/                  # Main package
│   ├── __init__.py            # Package initialization
│   ├── bench.py               # Core benchmarking functions
│   ├── bench_old.py           # Legacy code (reference)
│   └── cli.py                 # Command-line interface
├── tests/
│   ├── __init__.py
│   └── test_bench.py          # Comprehensive unit tests
├── scripts/
│   └── audit.py               # Code quality audit script
├── pyproject.toml             # Project configuration
├── requirements.txt           # Dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Code Quality Standards

This project maintains high code quality standards:

- **Linting**: flake8 for style checking
- **Formatting**: black for consistent code formatting  
- **Import Sorting**: isort for organized imports
- **Type Checking**: mypy for static type analysis
- **Testing**: pytest with 80%+ coverage requirement
- **Security**: bandit and safety for security scanning

## Continuous Integration

The project uses GitHub Actions for CI/CD with the following checks:

- ✅ **Multi-Python Testing**: Tests against Python 3.8-3.12
- ✅ **Code Quality**: Linting, formatting, and type checking
- ✅ **Test Coverage**: Minimum 80% coverage requirement
- ✅ **Security Scanning**: Automated security vulnerability checks
- ✅ **Functional Testing**: CLI and module integration tests

## Legacy Code

The project includes `benchmark/bench_old.py` as a reference implementation showing the "before" state. This demonstrates:

- Poor variable naming and code organization
- Lack of type hints and documentation
- Hardcoded values and inflexible design
- Missing error handling and edge cases

Compare this with the modern implementation in `benchmark/bench.py` to see the improvements.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run the audit script: `python scripts/audit.py`
5. Ensure all tests pass and code quality checks succeed
6. Commit your changes: `git commit -am 'Add feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Changelog

### v1.0.0 (2024)
- Initial release with modern benchmarking capabilities
- Comprehensive test suite with 80%+ coverage
- CLI interface with multiple output formats
- GitHub Actions CI/CD pipeline
- Code quality automation with audit script
- Full documentation and examples
