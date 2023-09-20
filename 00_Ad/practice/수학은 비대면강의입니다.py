import sys

sys.stdin = open("수학은 비대면강의입니다.txt", "r")

a, b, c, d, e, f = map(int, input().split())
x = (f/e - c/b) / (a/b - d/e)
print(x)