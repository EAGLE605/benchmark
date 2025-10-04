"""Tests for the benchmark runner."""

from benchmark.core import Benchmark, BenchmarkResult
from benchmark.runner import BenchmarkRunner


def simple_func() -> int:
    """Simple test function."""
    return 42


def another_func() -> str:
    """Another test function."""
    return "hello"


def test_benchmark_runner_initialization() -> None:
    """Test BenchmarkRunner initialization."""
    runner = BenchmarkRunner()
    assert len(runner.benchmarks) == 0
    assert len(runner.results) == 0


def test_add_benchmark() -> None:
    """Test adding benchmarks to runner."""
    runner = BenchmarkRunner()
    benchmark = Benchmark("test", simple_func, iterations=1)

    runner.add_benchmark(benchmark)

    assert len(runner.benchmarks) == 1
    assert runner.benchmarks[0] == benchmark


def test_run_all_benchmarks() -> None:
    """Test running all benchmarks."""
    runner = BenchmarkRunner()

    benchmark1 = Benchmark(
        "test1", simple_func, iterations=1, measure_memory=False, measure_cpu=False
    )
    benchmark2 = Benchmark(
        "test2", another_func, iterations=1, measure_memory=False, measure_cpu=False
    )

    runner.add_benchmark(benchmark1)
    runner.add_benchmark(benchmark2)

    results = runner.run_all(verbose=False)

    assert len(results) == 2
    assert len(runner.results) == 2
    assert results[0].name == "test1"
    assert results[1].name == "test2"


def test_generate_report_no_results() -> None:
    """Test generating report with no results."""
    runner = BenchmarkRunner()
    report = runner.generate_report()
    assert "No benchmark results available" in report


def test_generate_report_with_results() -> None:
    """Test generating report with results."""
    runner = BenchmarkRunner()

    benchmark = Benchmark(
        "test", simple_func, iterations=1, measure_memory=False, measure_cpu=False
    )
    runner.add_benchmark(benchmark)
    runner.run_all(verbose=False)

    report = runner.generate_report()

    assert "Benchmark" in report
    assert "test" in report
    assert "Time" in report


def test_generate_report_sorting() -> None:
    """Test report generation with different sorting options."""
    runner = BenchmarkRunner()

    # Manually create results with different execution times
    result1 = BenchmarkResult("fast", 0.001)
    result2 = BenchmarkResult("slow", 0.010)

    runner.results = [result2, result1]  # Add in reverse order

    # Sort by execution time (default)
    report_time = runner.generate_report(sort_by="execution_time")
    assert "slow" in report_time
    assert "fast" in report_time

    # Sort by name
    report_name = runner.generate_report(sort_by="name")
    assert "fast" in report_name
    assert "slow" in report_name


def test_get_slowest() -> None:
    """Test getting slowest benchmarks."""
    runner = BenchmarkRunner()

    # Create results with different execution times
    runner.results = [
        BenchmarkResult("fast", 0.001),
        BenchmarkResult("medium", 0.005),
        BenchmarkResult("slow", 0.010),
        BenchmarkResult("very_slow", 0.020),
    ]

    slowest = runner.get_slowest(2)

    assert len(slowest) == 2
    assert slowest[0].name == "very_slow"
    assert slowest[1].name == "slow"


def test_get_slowest_no_results() -> None:
    """Test getting slowest benchmarks with no results."""
    runner = BenchmarkRunner()
    slowest = runner.get_slowest(5)
    assert len(slowest) == 0


def test_get_memory_intensive() -> None:
    """Test getting memory-intensive benchmarks."""
    runner = BenchmarkRunner()

    # Create results with different memory usage
    runner.results = [
        BenchmarkResult("low_memory", 0.001, memory_usage=1024),
        BenchmarkResult("high_memory", 0.001, memory_usage=8192),
        BenchmarkResult("no_memory", 0.001, memory_usage=None),
        BenchmarkResult("medium_memory", 0.001, memory_usage=4096),
    ]

    memory_intensive = runner.get_memory_intensive(2)

    assert len(memory_intensive) == 2
    assert memory_intensive[0].name == "high_memory"
    assert memory_intensive[1].name == "medium_memory"


def test_get_memory_intensive_no_results() -> None:
    """Test getting memory-intensive benchmarks with no results."""
    runner = BenchmarkRunner()
    memory_intensive = runner.get_memory_intensive(5)
    assert len(memory_intensive) == 0


def test_clear() -> None:
    """Test clearing benchmarks and results."""
    runner = BenchmarkRunner()

    benchmark = Benchmark("test", simple_func, iterations=1)
    runner.add_benchmark(benchmark)
    runner.run_all(verbose=False)

    assert len(runner.benchmarks) == 1
    assert len(runner.results) == 1

    runner.clear()

    assert len(runner.benchmarks) == 0
    assert len(runner.results) == 0


def test_run_all_verbose_output(capsys) -> None:
    """Test verbose output during benchmark run."""
    runner = BenchmarkRunner()

    benchmark = Benchmark(
        "test", simple_func, iterations=1, measure_memory=False, measure_cpu=False
    )
    runner.add_benchmark(benchmark)

    runner.run_all(verbose=True)

    captured = capsys.readouterr()
    assert "Running benchmark 1/1: test" in captured.out
    assert "Time:" in captured.out


def test_generate_report_invalid_sort_field() -> None:
    """Test report generation with invalid sort field."""
    runner = BenchmarkRunner()

    result = BenchmarkResult("test", 0.001)
    runner.results = [result]

    # Should not crash with invalid sort field
    report = runner.generate_report(sort_by="invalid_field")
    assert "test" in report
