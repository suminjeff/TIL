import sys

sys.stdin = open("파스칼의 삼각형.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for col in range(1):
        for row in range(N):
            arr[row][col] = 1
    for row in range(1, N):
        for col in range(1, row+1):
            arr[row][col] = arr[row-1][col-1] + arr[row-1][col]

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                print(arr[i][j], end=" ")
        print()