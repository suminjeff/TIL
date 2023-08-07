import sys
sys.stdin = open("직사각형 네개의 합집합의 면적 구하기.txt", "r")

T = 4
N = 100

arr = [[False]*N for _ in range(N)]
for _ in range(1, T+1):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(y1, y2):
        for col in range(x1, x2):
            arr[row][col] = True

count = 0
for row in range(N):
    for col in range(N):
        if arr[row][col]:
            count += 1
print(count)