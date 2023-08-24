import sys

sys.stdin = open('색종이.txt', 'r')

arr = [[0]*1001 for _ in range(1001)]

N = int(input())
for i in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for row in range(x, x+w):
        for col in range(y, y+h):
            arr[row][col] = i

for j in range(1, N+1):
    cnt = 0
    for row in range(1001):
        for col in range(1001):
            if arr[row][col] == j:
                cnt += 1
    print(cnt)
