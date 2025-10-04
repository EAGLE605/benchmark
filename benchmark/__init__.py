"""Benchmark package for performance testing and measurement."""

__version__ = "0.1.0"
__author__ = "EAGLE605"
__email__ = "eagle605@example.com"

from .core import Benchmark, BenchmarkResult
from .runner import BenchmarkRunner
from .utils import format_duration, format_memory

__all__ = [
    "Benchmark",
    "BenchmarkResult",
    "BenchmarkRunner",
    "format_duration",
    "format_memory",
]
"""Benchmarking package for product performance measurement."""

__version__ = "1.0.0"
__author__ = "EAGLE605"

from .bench import measure_products, measure_work

__all__ = ["measure_work", "measure_products"]
