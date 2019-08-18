#!/usr/bin/env python
from typing import List, Dict


def get_all_values(N: int, v: int) -> List[int]:
    all_values = []

    current = v
    while current <= N:
        all_values.append(current)
        current *= v

    return all_values


def get_min_number(memo: Dict[int, int], all_values: List[int], N: int) -> int:
    if N in memo:
        return memo[N]

    if N in all_values:
        return 1
    elif N < 6:
        return N
    else:
        min_number: int = min(
            [get_min_number(memo, all_values, N - v) + 1 for v in all_values if N - v >= 0]
        )
        memo[N] = min_number
        return min_number


def solve(N: int) -> int:
    # Get all values and sort in descent order
    all_values: List[int] = [1] + get_all_values(N, 6) + get_all_values(N, 9)
    sorted_all_values: List[int] = list(reversed(sorted(all_values)))

    # Recursively get minimum number
    memo: Dict[int, int] = {}
    ans = get_min_number(memo, sorted_all_values, N)

    return ans


def main():
    # Input
    N = int(input())

    # Solve
    ans = solve(N)

    # Answer
    print(ans)


if __name__ == "__main__":
    main()
