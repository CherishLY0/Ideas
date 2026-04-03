import itertools
import math
import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(tempfile.gettempdir()) / "compiled-java-classes"


def compile_java():
    javac = shutil.which("javac")
    assert javac, "javac not found"
    OUT.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [javac, "-encoding", "UTF-8", "-d", str(OUT), str(ROOT / "Solution.java")],
        check=True,
        cwd=ROOT,
    )


@pytest.fixture(scope="module", autouse=True)
def build_java():
    compile_java()


def run_case(data):
    result = subprocess.run(
        ["java", "-cp", str(OUT), "Solution"],
        input=data,
        text=True,
        capture_output=True,
        cwd=ROOT,
        check=True,
    )
    return float(result.stdout.strip())


def brute_force(axis_points, head, start_index):
    points = [(x, 0.0) for x in axis_points] + [head]
    target_mask = (1 << len(points)) - 1
    dist = [
        [
            math.hypot(points[i][0] - points[j][0], points[i][1] - points[j][1])
            for j in range(len(points))
        ]
        for i in range(len(points))
    ]
    best = math.inf
    stack = [(start_index, 1 << start_index, 0.0)]
    seen = {}

    while stack:
        node, mask, cost = stack.pop()
        if cost >= seen.get((node, mask), math.inf):
            continue
        seen[(node, mask)] = cost
        if mask == target_mask:
            best = min(best, cost)
            continue
        for nxt in range(len(points)):
            nxt_mask = mask | (1 << nxt)
            nxt_cost = cost + dist[node][nxt]
            if nxt_cost < best:
                stack.append((nxt, nxt_mask, nxt_cost))
    return best


def test_sample_case_one():
    assert abs(run_case("3 1\n1 0 2\n1 1\n") - 3.828427) < 1e-6


def test_sample_case_two():
    assert abs(run_case("4 1\n0 5 -1 -5\n2 3\n") - 16.858414) < 1e-6


def test_small_cases_match_brute_force():
    axis_cases = [[0, 2], [0, 2, 5], [-3, 0, 4], [-2, 1, 3, 6]]
    head_cases = [(1, 1), (2, 3), (-1, 2)]
    for axis_points, head in itertools.product(axis_cases, head_cases):
        n = len(axis_points)
        for start in range(n + 1):
            data = f"{n} {start + 1}\n{' '.join(map(str, axis_points))}\n{head[0]} {head[1]}\n"
            assert abs(run_case(data) - brute_force(axis_points, head, start)) < 1e-6
