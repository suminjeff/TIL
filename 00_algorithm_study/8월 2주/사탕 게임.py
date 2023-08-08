import sys

sys.stdin = open("사탕 게임.txt", "r")

N = int(input())
arr = [input() for _ in range(N)]

print(arr)