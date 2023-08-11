import sys

sys.stdin = open("어디에 단어가 들어갈 수 있을까.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 1
    for row in range(N):
        temp = 1
        for col in range(N - 1):
            if arr[row][col] == arr[row][col + 1] == 1:
                temp += 1
            else:
                temp = 1
        if temp == K:
            cnt += 1

    for col in range(N):
        temp = 1
        for row in range(N - 1):
            if arr[row][col] == arr[row+1][col] == 1:
                temp += 1
            else:
                temp = 1
        if temp == K:
            cnt += 1

    print(f"#{tc} {cnt}")