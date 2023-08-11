import sys
sys.stdin = open("고대 유적.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_len = 1
    for row in range(N):
        count = 1
        for col in range(M-1):
            if arr[row][col] == arr[row][col+1] == 1:
                count += 1
        if max_len < count:
            max_len = count
    for col in range(M):
        count = 1
        for row in range(N - 1):
            if arr[row][col] == arr[row+1][col] == 1:
                count += 1
        if max_len < count:
            max_len = count
    print(f"#{tc} {max_len}")
