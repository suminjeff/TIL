import sys
sys.stdin = open("대지.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_x, max_y, min_x, min_y = -10000, -10000, 10000, 10000
for r in range(N):
    x, y = arr[r][0], arr[r][1]
    max_x, max_y = max(max_x, x), max(max_y, y)
    min_x, min_y = min(min_x, x), min(min_y, y)
ans = (max_x - min_x) * (max_y - min_y)
print(ans)