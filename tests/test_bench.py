import time

from benchmark.bench import measure_work, measure_products


def test_measure_work_quick():
    def work():
        # quick work: sleep a tiny amount
        time.sleep(0.001)

    elapsed = measure_work(work)
    assert elapsed >= 0.0


def test_measure_products_counts():
    prods = ["X", "Y"]
    results = measure_products(prods, iterations=10)
    assert set(results.keys()) == set(prods)
    assert all(v >= 0.0 for v in results.values())


def test_measure_products_zero_iterations():
    prods = ["Z"]
    results = measure_products(prods, iterations=0)
    # should still return a measurement (fast but >= 0)
    assert "Z" in results
    assert results["Z"] >= 0.0
