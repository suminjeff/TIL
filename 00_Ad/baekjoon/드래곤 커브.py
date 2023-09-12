import sys

sys.stdin = open("드래곤 커브.txt", "r")


direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]


def dragon_curve(coors):
    b, a = coors.pop()
    while coors:
        d, c = coors.pop()





def get_ans():
    pass


N = int(input())
grid = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    grid[y][x] = 1
    stack = [[y, x]]
    # 0=우, 1=상, 2=좌, 3=하
    for gen in range(g):
        if gen == 0:
            dy, dx = direction[d][0], direction[d][1]
            ny, nx = y+dy, x+dx
            grid[ny][nx] = 1
            stack.append([ny, nx])
        else:
            dragon_curve(stack)
