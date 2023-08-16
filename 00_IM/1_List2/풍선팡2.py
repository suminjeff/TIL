import sys

sys.stdin = open("풍선팡2.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_v = 0
    for i in range(N):
        for j in range(M):
            pang = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    pang += arr[ni][nj]
            if max_v < pang:
                max_v = pang

    print(f"#{tc} {max_v}")