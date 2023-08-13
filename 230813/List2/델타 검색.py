import sys

sys.stdin = open("델타 검색.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    delta_sum = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    temp = arr[i][j] - arr[nr][nc]
                    if temp >= 0:
                        delta_sum += temp
                    else:
                        delta_sum -= temp

    print(f"#{tc} {delta_sum}")