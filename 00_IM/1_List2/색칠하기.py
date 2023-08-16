import sys

sys.stdin = open("색칠하기.txt", "r")

T = int(input())

for tc in range(1, T+1):
    arr = [[0]*10 for _ in range(10)]
    N = int(input())
    cnt = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if arr[i][j] == 0:
                    arr[i][j] = color
                else:
                    arr[i][j] = 3
                    cnt += 1
    print(f"#{tc} {cnt}")
