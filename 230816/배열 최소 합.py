import sys

sys.stdin = open("배열 최소 합.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    given = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    