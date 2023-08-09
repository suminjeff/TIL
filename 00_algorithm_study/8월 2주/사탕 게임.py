import sys
sys.stdin = open("사탕 게임.txt", "r")

N = int(input())
arr = [list(input()) for _ in range(N)]
max_len = 0
for row in range(N):
    for col in range(N-1):
        if arr[row][col]
        arr[row][col], arr[row][col+1] = arr[row][col+1], arr[row][col]
        print(arr)
    print()