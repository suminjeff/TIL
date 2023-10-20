import sys
sys.stdin = open('어린 왕자.txt', 'r')
input = sys.stdin.readline
from collections import deque
from math import sqrt


def in_circle(x, y):
    res = [0]*N
    for i in range(N):
        px, py, pr = planets[i]
        d = sqrt((x-px)**2 + (y-py)**2)
        if d < pr:
            res[i] += 1
    return res


T = int(input())
for tc in range(1, T+1):
    sx, sy, ex, ey = map(int, input().split())
    N = int(input())
    planets = [list(map(int, input().split())) for _ in range(N)]
    start_in_circle = in_circle(sx, sy)
    target_in_circle = in_circle(ex, ey)
    cnt = 0
    for i in range(N):
        if start_in_circle[i] != target_in_circle[i]:
            cnt += 1
    print(cnt)