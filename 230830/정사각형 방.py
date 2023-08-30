import sys
# import time
sys.stdin = open("정사각형 방.txt", "r")
sys.setrecursionlimit(10**6)

# start_time = time.time()


def my_sum(vstd):
    global N
    ans = 0
    for x in range(N):
        for y in range(N):
            ans += vstd[x][y]
    return ans


def my_max(result):
    max_v = 0
    start = 0
    for x in result:
        if max_v < x[1]:
            max_v = x[1]
            start = x[0]
    return [start, max_v]


def dfs(r, c):
    global N
    global cnt
    # visited[r][c] = 1
    cnt += 1
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            # if arr[r][c] + 1 == arr[nr][nc] and visited[nr][nc] == 0:
            if arr[r][c] + 1 == arr[nr][nc]:
                dfs(nr, nc)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    res = []
    for i in range(N):
        for j in range(N):
            cnt = 0
            # visited = [[0]*N for _ in range(N)]
            dfs(i, j)
            res.append([arr[i][j], cnt])
    res.sort()
    print(f"#{tc}", *my_max(res))
# end_time = time.time()
# print(end_time - start_time)