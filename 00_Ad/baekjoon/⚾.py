import sys
from itertools import permutations

sys.stdin = open("⚾.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lineup_idx = [n for n in range(9)]
possible_lineup = []

# 타순 순열 나누기
for perm in permutations(lineup_idx, 9):
    if perm[3] == 0:
        possible_lineup.append(perm)

max_points = 0
for lineup in possible_lineup:
    inning = 0
    out_cnt = 0
    points = 0
    base = [0] * 4
    order = 0
    while inning < N:
        batter = arr[inning][lineup[order]]
        if batter == 0:
            out_cnt += 1
            if out_cnt % 3 == 0:
                inning += 1
        elif batter == 1:
            points += base[3]
            base[3], base[2], base[1] = base[2], base[1], 1
        elif batter == 2:
            points += base[3] + base[2]
            base[3], base[2], base[1] = base[1], 1, 0
        elif batter == 3:
            points += base[3] + base[2] + base[1]
            base[3], base[2], base[1] = 1, 0, 0
        elif batter == 4:
            points += base[3] + base[2] + base[1] + 1
            base[3], base[2], base[1] = 0, 0, 0
        order = (order + 1) % 9
    if max_points < points:
        max_points = points
        # print(lineup, points)
print(max_points)
