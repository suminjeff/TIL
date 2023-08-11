import sys

sys.stdin = open("풍선팡.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    max_result = 0
    for row in range(N):
        for col in range(M):
            v = arr[row][col]
            result = 0
            result += v
            for delta in range(4):
                for pang in range(1, v+1):
                    nr = row + dr[delta] * pang
                    nc = col + dc[delta] * pang
                    if 0 <= nr < N and 0 <= nc < M:
                        result += arr[nr][nc]
            if max_result < result:
                max_result = result

    print(f"#{tc} {max_result}")


