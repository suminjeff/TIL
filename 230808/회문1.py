import sys

sys.stdin = open("회문1.txt", "r", encoding="utf-8")

T = 10
N = 8
for tc in range(1, T+1):
    M = int(input())
    arr = [input() for _ in range(N)]

    count = 0
    for row in range(N):
        for col in range(N-M+1):
            temp = ""
            for c in range(col, col+M):
                temp += arr[row][c]
            if temp == temp[::-1]:
                count += 1

    for col in range(N):
        for row in range(N-M+1):
            temp = ""
            for r in range(row, row+M):
                temp += arr[r][col]
            if temp == temp[::-1]:
                count += 1

    print(f"#{tc} {count}")
