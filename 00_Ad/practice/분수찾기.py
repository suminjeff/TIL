import sys

sys.stdin = open("분수찾기.txt", "r")

N = int(input())

cnt = 1
numerator, denominator = 1, 1

while cnt != N:
    numerator += 1
    for i in range(numerator, 1, -1):
        numerator -= 1
        denominator += 1
        cnt += 1
ans = f"{numerator} / {denominator}"
print(ans)