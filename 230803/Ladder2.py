import sys

sys.stdin = open("ladder.txt", "r")

T = 10

for _ in range(1, T + 1):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 마지막 줄에서 x 찾기
    col = 0
    for x in range(N):
        if arr[N - 1][x] == 2:
            col = x
            break

    dr = [0, 0, -1]
    dc = [-1, 1, 0]
    row = N - 1

    while row > 0:
        for d_idx in range(3):
            nr = row + dr[d_idx]
            nc = col + dc[d_idx]
            if (0 <= nr < N) and (0 <= nc < N) and (arr[nr][nc] == 1):
                row = nr
                col = nc
                break

    print(f'#{tc} {col}')
