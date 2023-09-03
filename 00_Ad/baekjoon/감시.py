import sys
import copy

sys.stdin = open("감시.txt", "r")


direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]]
}


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cctv_types = [n for n in range(1, 6)]
coor = []
zero = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


for i in range(N):
    for j in range(M):
        if arr[i][j] in cctv_types:
            coor.append((i, j))

for r, c in coor:


# print(arr)