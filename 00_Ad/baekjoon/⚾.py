import sys

sys.stdin = open("⚾.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for n in range(1, 9):
    lineup = [[[] for _ in range(9)] for _ in range(N)]
    ordering = n
    for r in range(N):
        for c in range(9):
            lineup[r][c] =


    inning = 0
    out_cnt = 0
    points = 0
    base = [0] * 4
    home = 0
    rear = 0
    order = n
    while inning < N:
        if order == (n + 3) % 9:
            batter = arr[inning][order]
        else:
            batter = arr[inning][order]
        if batter == 0:
            out_cnt += 1
            if out_cnt % 3 == 0:
                inning += 1
        else:
            for _ in range(batter):
                if home == 0:
                    home = 3
                else:
                    home -= 1
                if base[home] == 1:
                    points += 1
            rear = (home + batter) % 4
            base[rear] = 1
            if base[home] == 1:
                points += 1
                base[home] = 0
        if order == (n + 3) % 9:
            order = (n + 4) % 9
        else:
            order = (order + 1) % 9
    print(points)
