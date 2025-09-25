"""Tests for utility functions."""

from benchmark.utils import (
    calculate_performance_ratio,
    format_duration,
    format_memory,
    validate_benchmark_name,
)


class TestFormatDuration:
    """Test duration formatting functionality."""

    def test_nanoseconds(self) -> None:
        """Test nanosecond formatting."""
        result = format_duration(5e-9)
        assert result == "5.00 ns"

    def test_microseconds(self) -> None:
        """Test microsecond formatting."""
        result = format_duration(150e-6)
        assert result == "150.00 μs"

    def test_milliseconds(self) -> None:
        """Test millisecond formatting."""
        result = format_duration(0.25)
        assert result == "250.00 ms"

    def test_seconds(self) -> None:
        """Test second formatting."""
        result = format_duration(5.5)
        assert result == "5.50 s"

    def test_minutes(self) -> None:
        """Test minute formatting."""
        result = format_duration(125.75)
        assert result == "2m 5.75s"


class TestFormatMemory:
    """Test memory formatting functionality."""

    def test_none_value(self) -> None:
        """Test None memory value."""
        result = format_memory(None)
        assert result == "N/A"

    def test_bytes(self) -> None:
        """Test byte formatting."""
        result = format_memory(512)
        assert result == "512 B"

    def test_kilobytes(self) -> None:
        """Test kilobyte formatting."""
        result = format_memory(2048)
        assert result == "2.00 KB"

    def test_megabytes(self) -> None:
        """Test megabyte formatting."""
        result = format_memory(5 * 1024 * 1024)
        assert result == "5.00 MB"

    def test_gigabytes(self) -> None:
        """Test gigabyte formatting."""
        result = format_memory(3 * 1024 * 1024 * 1024)
        assert result == "3.00 GB"


class TestValidateBenchmarkName:
    """Test benchmark name validation."""

    def test_valid_names(self) -> None:
        """Test valid benchmark names."""
        valid_names = [
            "test_benchmark",
            "TestBenchmark",
            "test-benchmark",
            "test benchmark",
            "benchmark_123",
            "simple",
        ]

        for name in valid_names:
            assert validate_benchmark_name(name), f"Name '{name}' should be valid"

    def test_invalid_names(self) -> None:
        """Test invalid benchmark names."""
        invalid_names = [
            "",  # Empty string
            "test@benchmark",  # Special characters
            "test$benchmark",  # Special characters
            "test#benchmark",  # Special characters
            "a" * 101,  # Too long
        ]

        for name in invalid_names:
            assert not validate_benchmark_name(name), f"Name '{name}' should be invalid"


class TestCalculatePerformanceRatio:
    """Test performance ratio calculation."""

    def test_normal_ratio(self) -> None:
        """Test normal performance ratio calculation."""
        ratio = calculate_performance_ratio(10.0, 5.0)
        assert ratio == 2.0

    def test_equal_values(self) -> None:
        """Test performance ratio with equal values."""
        ratio = calculate_performance_ratio(5.0, 5.0)
        assert ratio == 1.0

    def test_baseline_zero_current_zero(self) -> None:
        """Test performance ratio with both values zero."""
        ratio = calculate_performance_ratio(0.0, 0.0)
        assert ratio == float("inf")

    def test_baseline_zero_current_nonzero(self) -> None:
        """Test performance ratio with zero baseline."""
        ratio = calculate_performance_ratio(0.0, 5.0)
        assert ratio == 0.0

    def test_worse_performance(self) -> None:
        """Test performance ratio when current is slower."""
        ratio = calculate_performance_ratio(5.0, 10.0)
        assert ratio == 0.5
