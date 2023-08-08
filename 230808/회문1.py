import sys

sys.stdin = open("회문1.txt", "r", encoding="utf-8")


def my_len(iterable):
    length = 0
    for _ in iterable:
        length += 1
    return length


def palindrome(string):
    n = my_len(string)
    for i in range(n//2):
        if string[i] != string[n-1-i]:
            return False
    return True


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
            if palindrome(temp):
                count += 1

    for col in range(N):
        for row in range(N-M+1):
            temp = ""
            for r in range(row, row+M):
                temp += arr[r][col]
            if palindrome(temp):
                count += 1

    print(f"#{tc} {count}")
