"""Utility functions for benchmarking."""

from typing import Optional


def format_duration(seconds: float) -> str:
    """Format duration in seconds to human-readable string.

    Args:
        seconds: Duration in seconds

    Returns:
        Formatted duration string
    """
    if seconds < 1e-6:
        return f"{seconds * 1e9:.2f} ns"
    elif seconds < 1e-3:
        return f"{seconds * 1e6:.2f} μs"
    elif seconds < 1:
        return f"{seconds * 1e3:.2f} ms"
    elif seconds < 60:
        return f"{seconds:.2f} s"
    else:
        minutes = int(seconds // 60)
        remaining_seconds = seconds % 60
        return f"{minutes}m {remaining_seconds:.2f}s"


def format_memory(bytes_used: Optional[int]) -> str:
    """Format memory usage in bytes to human-readable string.

    Args:
        bytes_used: Memory usage in bytes

    Returns:
        Formatted memory string
    """
    if bytes_used is None:
        return "N/A"

    if bytes_used < 1024:
        return f"{bytes_used} B"
    elif bytes_used < 1024**2:
        return f"{bytes_used / 1024:.2f} KB"
    elif bytes_used < 1024**3:
        return f"{bytes_used / (1024 ** 2):.2f} MB"
    else:
        return f"{bytes_used / (1024 ** 3):.2f} GB"


def validate_benchmark_name(name: str) -> bool:
    """Validate that a benchmark name follows naming conventions.

    Args:
        name: Benchmark name to validate

    Returns:
        True if name is valid, False otherwise
    """
    if not name:
        return False

    # Name should be alphanumeric with underscores and hyphens
    if not name.replace("_", "").replace("-", "").replace(" ", "").isalnum():
        return False

    # Name should not be too long
    if len(name) > 100:
        return False

    return True


def calculate_performance_ratio(baseline: float, current: float) -> float:
    """Calculate performance ratio between baseline and current measurement.

    Args:
        baseline: Baseline measurement
        current: Current measurement

    Returns:
        Performance ratio (higher is better for time, lower is better for memory)
    """
    if baseline == 0:
        return float("inf") if current == 0 else 0.0

    return baseline / current
