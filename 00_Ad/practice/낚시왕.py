import sys
sys.stdin = open('낚시왕.txt', 'r')
input = sys.stdin.readline
from collections import deque


def catch(k, shark_que):
    visited = [[0]*C for _ in range(R)]
    que = deque()
    que.append([0, k])




def shark(que):
    res = deque()
    while que:
        r, c, s, d, z = que.popleft()
        arr[r][c][d] = []
        sharks[r][c] -= 1
        if d == 0:
            moving = s % R
        elif d == 1:
            r = (r+s)%(2*(R-1))
        elif d == 2:
            c = (c+s)%(2*(C-1))
        elif d == 3:
            s -= c
            c = s%(2*(C-1))


    pass




R, C, M = map(int, input().split())
que = deque()
delta = {
    0: [-1, 0, 1],
    1: [1, 0, 0],
    2: [0, 1, 3],
    3: [0, -1, 2],
}
arr = [[[[] for _ in range(4)] for _ in range(C)] for _ in range(R)]
sharks = [[0]*C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    que.append((r-1, c-1, s, d-1, z))
    arr[r-1][c-1][d-1].append([s, z])
    sharks[r-1][c-1] += 1
print(que)
print(arr)
# K = 0
# while K < C:
#     catch()
#     shark()
#     K += 1
