import sys
sys.stdin = open('터렛.txt', 'r')
input = sys.stdin.readline
from math import sqrt

def circle(x1, x2, y1, y2, r1, r2):
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            return -1
        elif r1 != r2:
            return 0
    distance = sqrt((x1-x2)**2 + (y1-y2)**2)
    radius_sum = r1+r2
    if distance > radius_sum:
        return 0
    elif distance == radius_sum or distance + min(r1, r2) == max(r1, r2):
        return 1
    else:
        if max(r1, r2) == min(r1, r2) + distance:
            return 1
        elif max(r1, r2) > min(r1, r2) + distance:
            return 0
        else:
            return 2



T = int(input())
for tc in range(1, T + 1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(circle(x1, x2, y1, y2, r1, r2))
