import sys

sys.stdin = open("2048 (Easy).txt", "r")


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

