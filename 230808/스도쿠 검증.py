import sys

sys.stdin = open("스도쿠 검증.txt", "r", encoding="utf-8")


def my_count(arr, k):
    count = 0
    for i in arr:
        if i == k:
            count += 1
    return count


T = int(input())
N = 9
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = True

    for row in range(N):
        total = 0
        temp = []
        for col in range(N):
            total += arr[row][col]
            temp.append(arr[row][col])
        for k in temp:
            if my_count(temp, k) > 1:
                ans = False

    for col in range(N):
        total = 0
        temp = []
        for row in range(N):
            total += arr[row][col]
            temp.append(arr[row][col])
        for k in temp:
            if my_count(temp, k) > 1:
                ans = False

    for row in range(0, N, N//3):
        for col in range(0, N, N//3):
            total = 0
            temp = []
            for r in range(row, row + N//3):
                for c in range(col, col + N//3):
                    total += arr[r][c]
                    temp.append(arr[r][c])
            for k in temp:
                if my_count(temp, k) > 1:
                    ans = False

    print(f"#{tc} {int(ans)}")
