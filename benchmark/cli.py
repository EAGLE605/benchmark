"""Command line interface for the benchmark tool."""

import sys
from typing import List

import click

from .core import Benchmark
from .runner import BenchmarkRunner


def example_function_fast() -> int:
    """Fast example function for demonstration."""
    return sum(range(1000))


def example_function_slow() -> int:
    """Slow example function for demonstration."""
    return sum(range(100000))


def example_function_memory() -> List[int]:
    """Memory-intensive example function for demonstration."""
    return list(range(50000))


@click.command()
@click.option(
    "--iterations",
    "-i",
    default=10,
    help="Number of iterations to run each benchmark",
    type=int,
)
@click.option(
    "--sort-by",
    "-s",
    default="execution_time",
    help="Sort results by field (execution_time, memory_usage, name)",
    type=click.Choice(["execution_time", "memory_usage", "name"]),
)
@click.option(
    "--no-memory",
    is_flag=True,
    help="Disable memory usage measurement",
)
@click.option(
    "--no-cpu",
    is_flag=True,
    help="Disable CPU usage measurement",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Enable verbose output",
)
def main(
    iterations: int,
    sort_by: str,
    no_memory: bool,
    no_cpu: bool,
    verbose: bool,
) -> None:
    """Run benchmark examples to demonstrate the benchmarking tool."""
    if iterations <= 0:
        click.echo("Error: Iterations must be positive", err=True)
        sys.exit(1)

    click.echo("🚀 Benchmark Tool - Performance Testing")
    click.echo("=" * 40)

    # Create benchmark runner
    runner = BenchmarkRunner()

    # Add example benchmarks
    benchmarks_config = [
        ("Fast Function", example_function_fast),
        ("Slow Function", example_function_slow),
        ("Memory Intensive", example_function_memory),
    ]

    for name, func in benchmarks_config:
        benchmark = Benchmark(
            name=name,
            func=func,
            iterations=iterations,
            measure_memory=not no_memory,
            measure_cpu=not no_cpu,
        )
        runner.add_benchmark(benchmark)

    if verbose:
        click.echo(
            f"Running {len(runner.benchmarks)} benchmarks with {iterations} iterations each..."
        )
        click.echo()

    # Run benchmarks
    try:
        runner.run_all(verbose=verbose)

        # Generate and display report
        report = runner.generate_report(sort_by=sort_by)
        click.echo("📊 Benchmark Results:")
        click.echo(report)

        # Show top performers
        click.echo("\n🏆 Top 3 Fastest:")
        fastest = sorted(runner.results, key=lambda r: r.execution_time)[:3]
        for i, result in enumerate(fastest, 1):
            from .utils import format_duration

            click.echo(
                f"  {i}. {result.name}: {format_duration(result.execution_time)}"
            )

        if not no_memory:
            click.echo("\n💾 Top 3 Memory Efficient:")
            memory_efficient = sorted(
                [r for r in runner.results if r.memory_usage],
                key=lambda r: r.memory_usage or 0,
            )[:3]
            for i, result in enumerate(memory_efficient, 1):
                from .utils import format_memory

                click.echo(
                    f"  {i}. {result.name}: {format_memory(result.memory_usage)}"
                )

    except KeyboardInterrupt:
        click.echo("\n\nBenchmarking interrupted by user.", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"\nError running benchmarks: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()  # pragma: no cover
