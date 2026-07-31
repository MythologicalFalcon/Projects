"""Self-check for the KNN reduction. Run with: python test_reduce.py"""

import os
import sys
import tempfile

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src", "mainPackage"))
from reduceKNN import reduce_test_cases


def _write_csv(path, rows):
    pd.DataFrame(
        rows, columns=["Test Case", "Input", "Adequacy_Label", "f1", "f2"]
    ).to_csv(path, index=False)


def test_duplicates_are_dropped():
    """Three tight clusters of two should collapse to one row per cluster."""
    pairs = [(0, 0), (0, 0.01), (10, 10), (10, 10.01), (50, 50), (50, 50.01)]
    rows = [[f"tc{i}", f"in{i}", 1, x, y] for i, (x, y) in enumerate(pairs)]

    with tempfile.TemporaryDirectory() as d:
        src, dst = os.path.join(d, "in.csv"), os.path.join(d, "out.csv")
        _write_csv(src, rows)
        reduce_test_cases(src, dst, n_neighbors=2)
        out = pd.read_csv(dst)

    assert len(out) < len(rows), f"nothing was reduced: {len(out)} of {len(rows)}"
    assert len(out) == 3, f"expected one row per cluster, got {len(out)}"


def test_distinct_cases_are_kept():
    """Well-separated cases have no duplicates, so all of them survive."""
    rows = [[f"tc{i}", f"in{i}", 1, i * 100, i * 100] for i in range(5)]

    with tempfile.TemporaryDirectory() as d:
        src, dst = os.path.join(d, "in.csv"), os.path.join(d, "out.csv")
        _write_csv(src, rows)
        reduce_test_cases(src, dst, n_neighbors=1)
        out = pd.read_csv(dst)

    assert len(out) == len(rows), f"dropped distinct cases: {len(out)} of {len(rows)}"


if __name__ == "__main__":
    test_duplicates_are_dropped()
    test_distinct_cases_are_kept()
    print("OK")
