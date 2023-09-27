import sys
sys.stdin = open("RGB 거리.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for r in range(1, N):
    for c1 in range(3):
        min_v = 1000*N
        for c2 in range(3):
            if c1 != c2:
                min_v = min(min_v, arr[r-1][c2])
        arr[r][c1] += min_v
print(min(arr[-1]))