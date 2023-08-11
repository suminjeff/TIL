import sys

sys.stdin = open("풍선팡2.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    max_pang = 0
    for row in range(N):
        for col in range(M):
            v = arr[row][col]
            pang = 0
            pang += v
            for k in range(4):
                nr = row + dr[k]
                nc = col + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    pang += arr[nr][nc]
            if max_pang < pang:
                max_pang = pang

    print(f"#{tc} {max_pang}")

            # for k in range(4):
            #     for p in range(1, v+1):
            #         nr = row + dr[k] * v
            #         nc = col + dc[k] * v
            #         if 0 <= nr < N and 0 <= nc < N:
            #             pang += arr[nr][nc]
            # if max_pang < pang:
            #     max_pang = pang

