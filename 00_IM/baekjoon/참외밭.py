import sys

sys.stdin = open('참외밭.txt', 'r')

# K = 1제곱미터에 자라는 참외 개수
K = int(input())

max_h = 0
min_h = 501
max_w = 0
min_w = 501

for _ in range(6):
    d, m = map(int, input().split())
    if d == 1 or d == 2:
        if max_w < m:
            max_w = m
        if min_w > m:
            min_w = m
    if d == 3 or d == 4:
        if max_h < m:
            max_h = m
        if min_h > m:
            min_h = m

ans = K * (max_w * max_h - min_w * min_h)
print(ans)
print(max_w, max_h, min_w, min_h)