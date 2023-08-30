import sys

sys.stdin = open("최소합.txt", "r")

from itertools import permutations


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    num_of_moves = 2 * (N - 1)

    default_move = [0] * (N - 1) + [1] * (N - 1)
    min_sum = float("inf")

    for move in set(permutations(default_move, num_of_moves)):
        if sum(move) == num_of_moves // 2:
            r, c = 0, 0
            sum_of_nums = arr[r][c]
            for i in move:
                r += i
                c += 1-i
                sum_of_nums += arr[r][c]
            min_sum = min(min_sum, sum_of_nums)
    print(f"#{tc} {min_sum}")
