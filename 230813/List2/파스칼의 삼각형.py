import sys
sys.stdin = open("파스칼의 삼각형.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[1] + [0]*(N-1) for _ in range(N)]

    for i in range(1, N):
        for j in range(1, N):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                print(arr[i][j], end=" ")
        print()
