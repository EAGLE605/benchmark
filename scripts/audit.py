"""Simple audit runner: runs syntax checks (flake8) and unit tests (pytest).

This is intentionally minimal so it works in restricted CI/dev containers.
"""
import subprocess
import sys


def run(cmd: list[str]) -> int:
    print("Running:", " ".join(cmd))
    return subprocess.call(cmd)


def main() -> int:
    rc = 0
    # run flake8 if available
    try:
        rc = run([sys.executable, "-m", "flake8", "benchmark"])
    except Exception as exc:  # pragma: no cover - wrapper
        print("flake8 not available:", exc)

    # run pytest
    rc_tests = run([sys.executable, "-m", "pytest", "-q"])  # returns non-zero on failures
    if rc_tests != 0:
        print("Tests failed")
        return rc_tests
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
