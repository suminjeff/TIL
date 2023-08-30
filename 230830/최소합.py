import sys

sys.stdin = open("최소합.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            left = [i, j-1]
            right = [i-1, j]