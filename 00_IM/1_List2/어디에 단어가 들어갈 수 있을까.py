import sys

sys.stdin = open("어디에 단어가 들어갈 수 있을까.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 행탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if j == N-1 and cnt == K:
                    ans += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0

    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if i == N-1 and cnt == K:
                    ans += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
    print(f"#{tc} {ans}")
