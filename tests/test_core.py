"""Tests for the core benchmarking functionality."""

import time
from unittest.mock import patch

from benchmark.core import Benchmark, BenchmarkResult


def test_benchmark_result_initialization() -> None:
    """Test BenchmarkResult initialization."""
    result = BenchmarkResult(
        name="test",
        execution_time=1.5,
        memory_usage=1024,
        cpu_usage=50.0,
        iterations=10,
    )

    assert result.name == "test"
    assert result.execution_time == 1.5
    assert result.memory_usage == 1024
    assert result.cpu_usage == 50.0
    assert result.iterations == 10
    assert result.metadata == {}


def test_benchmark_result_default_metadata() -> None:
    """Test BenchmarkResult initializes metadata as empty dict."""
    result = BenchmarkResult(name="test", execution_time=1.0)
    assert result.metadata == {}


def simple_test_function() -> int:
    """Simple function for testing."""
    return 42


def slow_test_function() -> None:
    """Slow function for testing."""
    time.sleep(0.01)


def test_benchmark_initialization() -> None:
    """Test Benchmark initialization."""
    benchmark = Benchmark(
        name="test_benchmark",
        func=simple_test_function,
        iterations=5,
        measure_memory=True,
        measure_cpu=True,
    )

    assert benchmark.name == "test_benchmark"
    assert benchmark.func == simple_test_function
    assert benchmark.iterations == 5
    assert benchmark.measure_memory is True
    assert benchmark.measure_cpu is True
    assert benchmark.setup is None
    assert benchmark.teardown is None


def test_benchmark_run_basic() -> None:
    """Test basic benchmark execution."""
    benchmark = Benchmark(
        name="simple_test",
        func=simple_test_function,
        iterations=3,
        measure_memory=False,
        measure_cpu=False,
    )

    result = benchmark.run()

    assert result.name == "simple_test"
    assert result.execution_time > 0
    assert result.iterations == 3
    assert result.memory_usage is None
    assert result.cpu_usage is None


def test_benchmark_run_with_memory_tracking() -> None:
    """Test benchmark with memory tracking."""
    benchmark = Benchmark(
        name="memory_test",
        func=simple_test_function,
        iterations=1,
        measure_memory=True,
        measure_cpu=False,
    )

    result = benchmark.run()

    assert result.name == "memory_test"
    assert result.execution_time > 0
    assert result.memory_usage is not None
    assert result.memory_usage >= 0


def test_benchmark_with_setup_teardown() -> None:
    """Test benchmark with setup and teardown functions."""
    setup_called = []
    teardown_called = []

    def setup() -> None:
        setup_called.append(True)

    def teardown() -> None:
        teardown_called.append(True)

    benchmark = Benchmark(
        name="setup_teardown_test",
        func=simple_test_function,
        setup=setup,
        teardown=teardown,
        iterations=1,
        measure_memory=False,
        measure_cpu=False,
    )

    benchmark.run()

    assert len(setup_called) == 1
    assert len(teardown_called) == 1


def test_benchmark_with_arguments() -> None:
    """Test benchmark with function arguments."""

    def add_numbers(a: int, b: int) -> int:
        return a + b

    benchmark = Benchmark(
        name="args_test",
        func=add_numbers,
        iterations=1,
        measure_memory=False,
        measure_cpu=False,
    )

    result = benchmark.run(5, 10)

    assert result.name == "args_test"
    assert result.execution_time > 0


def test_benchmark_repr() -> None:
    """Test benchmark string representation."""
    benchmark = Benchmark(
        name="repr_test",
        func=simple_test_function,
        iterations=7,
    )

    repr_str = repr(benchmark)
    expected = "Benchmark(name='repr_test', iterations=7)"
    assert repr_str == expected


def test_benchmark_multiple_iterations() -> None:
    """Test benchmark with multiple iterations."""
    benchmark = Benchmark(
        name="multi_iteration_test",
        func=slow_test_function,
        iterations=3,
        measure_memory=False,
        measure_cpu=False,
    )

    result = benchmark.run()

    assert result.iterations == 3
    # Should take at least 0.03 seconds (3 * 0.01)
    assert result.execution_time >= 0.01  # Average per iteration


@patch("psutil.Process")
def test_benchmark_cpu_measurement(mock_process) -> None:
    """Test CPU usage measurement."""
    # Mock the process CPU measurement
    mock_instance = mock_process.return_value
    mock_instance.cpu_percent.side_effect = [10.0, 25.0]  # Start and end CPU

    benchmark = Benchmark(
        name="cpu_test",
        func=simple_test_function,
        iterations=1,
        measure_memory=False,
        measure_cpu=True,
    )

    result = benchmark.run()

    assert result.cpu_usage == 15.0  # 25.0 - 10.0
