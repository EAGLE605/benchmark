"""Benchmark runner for executing multiple benchmarks."""

from typing import List

from tabulate import tabulate

from .core import Benchmark, BenchmarkResult
from .utils import format_duration, format_memory


class BenchmarkRunner:
    """Runner for executing and reporting on multiple benchmarks."""

    def __init__(self) -> None:
        """Initialize the benchmark runner."""
        self.benchmarks: List[Benchmark] = []
        self.results: List[BenchmarkResult] = []

    def add_benchmark(self, benchmark: Benchmark) -> None:
        """Add a benchmark to the runner.

        Args:
            benchmark: Benchmark instance to add
        """
        self.benchmarks.append(benchmark)

    def run_all(self, verbose: bool = True) -> List[BenchmarkResult]:
        """Run all benchmarks and collect results.

        Args:
            verbose: Whether to print progress information

        Returns:
            List of BenchmarkResult instances
        """
        self.results = []

        for i, benchmark in enumerate(self.benchmarks, 1):
            if verbose:
                print(f"Running benchmark {i}/{len(self.benchmarks)}: {benchmark.name}")

            result = benchmark.run()
            self.results.append(result)

            if verbose:
                print(f"  Time: {format_duration(result.execution_time)}")
                if result.memory_usage:
                    print(f"  Memory: {format_memory(result.memory_usage)}")
                print()

        return self.results

    def generate_report(self, sort_by: str = "execution_time") -> str:
        """Generate a formatted report of benchmark results.

        Args:
            sort_by: Field to sort results by ('execution_time', 'memory_usage', 'name')

        Returns:
            Formatted report string
        """
        if not self.results:
            return "No benchmark results available. Run benchmarks first."

        # Sort results
        reverse_sort = sort_by != "name"
        try:
            sorted_results = sorted(
                self.results,
                key=lambda r: getattr(r, sort_by) or 0,
                reverse=reverse_sort,
            )
        except AttributeError:
            sorted_results = self.results

        # Prepare table data
        headers = ["Benchmark", "Time", "Memory", "CPU %", "Iterations"]
        table_data = []

        for result in sorted_results:
            row = [
                result.name,
                format_duration(result.execution_time),
                format_memory(result.memory_usage) if result.memory_usage else "N/A",
                f"{result.cpu_usage:.1f}" if result.cpu_usage else "N/A",
                str(result.iterations),
            ]
            table_data.append(row)

        return str(tabulate(table_data, headers=headers, tablefmt="grid"))

    def get_slowest(self, n: int = 5) -> List[BenchmarkResult]:
        """Get the N slowest benchmarks.

        Args:
            n: Number of slowest benchmarks to return

        Returns:
            List of the slowest BenchmarkResult instances
        """
        if not self.results:
            return []

        return sorted(self.results, key=lambda r: r.execution_time, reverse=True)[:n]

    def get_memory_intensive(self, n: int = 5) -> List[BenchmarkResult]:
        """Get the N most memory-intensive benchmarks.

        Args:
            n: Number of memory-intensive benchmarks to return

        Returns:
            List of the most memory-intensive BenchmarkResult instances
        """
        if not self.results:
            return []

        memory_results = [r for r in self.results if r.memory_usage is not None]
        return sorted(memory_results, key=lambda r: r.memory_usage or 0, reverse=True)[
            :n
        ]

    def clear(self) -> None:
        """Clear all benchmarks and results."""
        self.benchmarks.clear()
        self.results.clear()
