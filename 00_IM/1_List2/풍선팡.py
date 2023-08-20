import sys

sys.stdin = open("풍선팡.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    ans = 0
    for i in range(N):
        for j in range(M):
            pang = arr[i][j]
            boom = pang
            for k in range(4):
                for p in range(1, boom+1):
                    ni = i + di[k] * p
                    nj = j + dj[k] * p
                    if 0 <= ni < N and 0 <= nj < M:
                        pang += arr[ni][nj]
            if ans < pang:
                ans = pang
    print(f"#{tc} {ans}")