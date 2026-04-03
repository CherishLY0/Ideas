import math
import sys


INF = float("inf")


def point_distance(x_value, head_x, head_y):
    return math.hypot(x_value - head_x, head_y)


def solve(data):
    values = list(map(int, data.split()))
    if not values:
        return ""

    n = values[0]
    k = values[1]
    axis_points = values[2:2 + n]
    head_x, head_y = values[2 + n], values[3 + n]

    sorted_points = sorted(axis_points)
    distances_to_head = [
        point_distance(point, head_x, head_y)
        for point in sorted_points
    ]

    no_head_left = [INF] * n
    no_head_right = [INF] * n
    yes_head_left = [INF] * n
    yes_head_right = [INF] * n
    yes_head_here = [INF] * n

    if k == n + 1:
        for index, distance in enumerate(distances_to_head):
            yes_head_left[index] = distance
            yes_head_right[index] = distance
    else:
        start_value = axis_points[k - 1]
        start_index = sorted_points.index(start_value)
        no_head_left[start_index] = 0.0
        no_head_right[start_index] = 0.0

    for length in range(1, n + 1):
        size = n - length + 1

        for left in range(size):
            right = left + length - 1
            yes_head_here[left] = min(
                yes_head_here[left],
                no_head_left[left] + distances_to_head[left],
                no_head_right[left] + distances_to_head[right],
            )

        if length == n:
            break

        next_no_head_left = [INF] * (size - 1)
        next_no_head_right = [INF] * (size - 1)
        next_yes_head_left = [INF] * (size - 1)
        next_yes_head_right = [INF] * (size - 1)
        next_yes_head_here = [INF] * (size - 1)

        for left in range(size):
            right = left + length - 1

            if left > 0:
                move_to_left = sorted_points[left] - sorted_points[left - 1]
                span_from_right = sorted_points[right] - sorted_points[left - 1]

                next_no_head_left[left - 1] = min(
                    next_no_head_left[left - 1],
                    no_head_left[left] + move_to_left,
                    no_head_right[left] + span_from_right,
                )
                next_yes_head_left[left - 1] = min(
                    next_yes_head_left[left - 1],
                    yes_head_left[left] + move_to_left,
                    yes_head_right[left] + span_from_right,
                    yes_head_here[left] + distances_to_head[left - 1],
                )

            if right + 1 < n:
                move_to_right = sorted_points[right + 1] - sorted_points[right]
                span_from_left = sorted_points[right + 1] - sorted_points[left]

                next_no_head_right[left] = min(
                    next_no_head_right[left],
                    no_head_right[left] + move_to_right,
                    no_head_left[left] + span_from_left,
                )
                next_yes_head_right[left] = min(
                    next_yes_head_right[left],
                    yes_head_right[left] + move_to_right,
                    yes_head_left[left] + span_from_left,
                    yes_head_here[left] + distances_to_head[right + 1],
                )

        no_head_left = next_no_head_left
        no_head_right = next_no_head_right
        yes_head_left = next_yes_head_left
        yes_head_right = next_yes_head_right
        yes_head_here = next_yes_head_here

    answer = min(yes_head_left[0], yes_head_right[0], yes_head_here[0])
    return f"{answer:.6f}"


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
