import sys

sys.stdin = open("중앙 이동 알고리즘.txt", "r")

N = int(input())
dots = 4
ans = dots
for i in range(N):
    side = int(dots**(1/2))
    side += side-1
    dots = side**2
    ans = dots
print(ans)
