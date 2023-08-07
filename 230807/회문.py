import sys
sys.stdin = open("회문.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans = ""
    for row in range(N):
        for col in range(N-M+1):
            temp = ""
            for k in range(col, col+M):
                temp += arr[row][k]
            if temp == temp[::-1]:
                ans = temp

    for col in range(N):
        for row in range(N-M+1):
            temp = ""
            for k in range(row, row+M):
                temp += arr[k][col]
            if temp == temp[::-1]:
                ans = temp

    print(f"#{tc} {ans}")