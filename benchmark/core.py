"""Core benchmarking functionality."""

import time
import tracemalloc
from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional

import psutil


@dataclass
class BenchmarkResult:
    """Result of a benchmark execution."""

    name: str
    execution_time: float
    memory_usage: Optional[int] = None
    cpu_usage: Optional[float] = None
    iterations: int = 1
    metadata: Optional[Dict[str, Any]] = None

    def __post_init__(self) -> None:
        """Initialize metadata if not provided."""
        if self.metadata is None:
            self.metadata = {}


class Benchmark:
    """A benchmark test case."""

    def __init__(
        self,
        name: str,
        func: Callable[..., Any],
        setup: Optional[Callable[..., Any]] = None,
        teardown: Optional[Callable[..., Any]] = None,
        iterations: int = 1,
        measure_memory: bool = True,
        measure_cpu: bool = True,
    ) -> None:
        """Initialize a benchmark.

        Args:
            name: Name of the benchmark
            func: Function to benchmark
            setup: Optional setup function to run before benchmarking
            teardown: Optional teardown function to run after benchmarking
            iterations: Number of times to run the benchmark
            measure_memory: Whether to measure memory usage
            measure_cpu: Whether to measure CPU usage
        """
        self.name = name
        self.func = func
        self.setup = setup
        self.teardown = teardown
        self.iterations = iterations
        self.measure_memory = measure_memory
        self.measure_cpu = measure_cpu

    def run(self, *args: Any, **kwargs: Any) -> BenchmarkResult:
        """Run the benchmark and return results.

        Args:
            *args: Arguments to pass to the benchmarked function
            **kwargs: Keyword arguments to pass to the benchmarked function

        Returns:
            BenchmarkResult containing timing and resource usage data
        """
        # Setup phase
        if self.setup:
            self.setup()

        total_time = 0.0
        memory_usage = None
        cpu_usage = None

        # Start memory tracking if requested
        if self.measure_memory:
            tracemalloc.start()

        # Start CPU monitoring if requested
        if self.measure_cpu:
            process = psutil.Process()
            cpu_start = process.cpu_percent()

        try:
            # Run benchmark iterations
            for _ in range(self.iterations):
                start_time = time.perf_counter()
                self.func(*args, **kwargs)
                end_time = time.perf_counter()
                total_time += end_time - start_time

            # Calculate average time per iteration
            avg_time = total_time / self.iterations

            # Get memory usage if tracking
            if self.measure_memory:
                current, peak = tracemalloc.get_traced_memory()
                memory_usage = peak
                tracemalloc.stop()

            # Get CPU usage if tracking
            if self.measure_cpu:
                cpu_usage = process.cpu_percent() - cpu_start

        finally:
            # Cleanup phase
            if self.teardown:
                self.teardown()

        return BenchmarkResult(
            name=self.name,
            execution_time=avg_time,
            memory_usage=memory_usage,
            cpu_usage=cpu_usage,
            iterations=self.iterations,
        )

    def __repr__(self) -> str:
        """String representation of the benchmark."""
        return f"Benchmark(name='{self.name}', iterations={self.iterations})"
