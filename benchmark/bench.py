"""Refactored benchmarking utilities for product performance measurement.

Provides a small, testable API: measure_work and measure_products.
"""
from __future__ import annotations

import time
from typing import Callable, Dict, Iterable


def measure_work(work: Callable[[], None]) -> float:
    """Measure the elapsed time (in seconds) for callable ``work``.

    Args:
        work: zero-argument callable performing the work to measure.

    Returns:
        float: elapsed seconds as a high-resolution timestamp difference.
    """
    start = time.perf_counter()
    work()
    end = time.perf_counter()
    return end - start


def measure_products(
    products: Iterable[str], iterations: int = 1000
) -> Dict[str, float]:
    """Measure a synthetic workload per product.

    The workload is intentionally trivial (a CPU-bound loop) so tests
    run quickly.

    Args:
        products: iterable of product identifiers.
        iterations: number of loop iterations for the synthetic workload.

    Returns:
        Mapping of product -> elapsed seconds.
    """

    def make_work(iters: int) -> Callable[[], None]:
        def _work() -> None:
            s = 0
            for i in range(iters):
                s += i * i

        return _work

    results: Dict[str, float] = {}
    for p in products:
        results[p] = measure_work(
            make_work(iterations)
        )
    return results


def main() -> None:
    products = ["A", "B", "C"]
    results = measure_products(products)
    for k, v in results.items():
        print(f"{k}: {v:.6f}s")


if __name__ == "__main__":
    main()
