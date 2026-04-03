import itertools
import math

from src.main import solve


def run_case(input_data):
    return float(solve(input_data))


def brute_force(axis_points, head, start_index):
    points = [(x, 0.0) for x in axis_points] + [head]
    target_mask = (1 << len(points)) - 1
    start_mask = 1 << start_index
    distances = [
        [
            math.hypot(points[i][0] - points[j][0], points[i][1] - points[j][1])
            for j in range(len(points))
        ]
        for i in range(len(points))
    ]

    best = math.inf
    stack = [(start_index, start_mask, 0.0)]
    seen = {}

    while stack:
        current, mask, cost = stack.pop()
        if cost >= seen.get((current, mask), math.inf):
            continue
        seen[(current, mask)] = cost

        if mask == target_mask:
            best = min(best, cost)
            continue

        for next_index in range(len(points)):
            next_mask = mask | (1 << next_index)
            next_cost = cost + distances[current][next_index]
            if next_cost < best:
                stack.append((next_index, next_mask, next_cost))

    return best


def test_sample_case_one():
    result = run_case("3 1\n1 0 2\n1 1\n")
    assert abs(result - 3.828427) < 1e-6


def test_sample_case_two():
    result = run_case("4 1\n0 5 -1 -5\n2 3\n")
    assert abs(result - 16.858414) < 1e-6


def test_small_cases_match_bruteforce():
    axis_cases = [
        [0, 2],
        [0, 2, 5],
        [-3, 0, 4],
        [-2, 1, 3, 6],
    ]
    head_cases = [(1.0, 1.0), (2.0, 3.0), (-1.0, 2.0)]

    for axis_points, head in itertools.product(axis_cases, head_cases):
        n = len(axis_points)
        for start in range(n + 1):
            input_data = (
                f"{n} {start + 1}\n"
                f"{' '.join(map(str, axis_points))}\n"
                f"{int(head[0])} {int(head[1])}\n"
            )
            expected = brute_force(axis_points, head, start)
            result = run_case(input_data)
            assert abs(result - expected) < 1e-6
