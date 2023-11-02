import sys
sys.stdin = open('색칠 1.txt', 'r')
input = sys.stdin.readline

W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

arr = [[1]*W + [0]*W for _ in range(H)]
for i in range(H):
    for j in range(f, f+f):
        arr[i][j] += 1

if c > 0:
    for i in range(c, H, c):
        for j in range(i, i+c):
            for k in range(f, W):
                arr[j][k] += arr[j-c][k]

print(*arr, sep='\n')

for i in range(y1, y2):
    for j in range(f+x1, f+x2):
        print(i, j)


# [6, 6, 3]
# [6, 6, 3]