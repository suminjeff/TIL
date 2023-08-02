import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0
    for row in range(N):
        for col in range(N):
            fly = 0
            for k in range(M):
                for j in range(M):
                    if 0 <= row+k < N and 0 <= col+j < N:
                        fly += arr[row+k][col+j]
                        if max_fly < fly:
                            max_fly = fly

    print(f"#{tc} {max_fly}")
