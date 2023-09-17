import sys

sys.stdin = open("분수찾기.txt", "r")

N = int(input())

cnt = 1
numerator, denominator = 1, 1

while True:
    M = denominator + 1
    numerator = M
    for i in range(1, M+1):
        numerator -= 1
        denominator = i
        cnt += 1
        if cnt == N:
            break
    numerator += 1

ans = f"{numerator}/{denominator}"
print(ans)