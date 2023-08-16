import sys

sys.stdin = open("Sum.txt", "r")

T = 10
N = 100
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N):
        row_sum = 0
        col_sum = 0
        cross_right = 0
        cross_left = 0
        for j in range(N):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            if i == j:
                cross_right += arr[i][j]
            if i == N - j - 1:
                cross_left += arr[i][j]
        if max_sum < row_sum:
            max_sum = row_sum
        if max_sum < col_sum:
            max_sum = col_sum
        if max_sum < cross_right:
            max_sum = cross_right
        if max_sum < cross_left:
            max_sum = cross_left
    print(f"#{tc} {max_sum}")