import sys

sys.stdin = open("수학은 비대면강의입니다.txt", "r")

a, b, c, d, e, f = map(int, input().split())

x = int((e*c-b*f)/(a*e-b*d))
y = int((d*c-a*f)/(b*d-a*e))

print(x, y)