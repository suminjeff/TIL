import sys
sys.stdin = open('파이프 옮기기 1.txt', 'r')
input = sys.stdin.readline


def dfs(r, c, p):
    global cnt

    if r == c == N-1:
        cnt += 1
        return

    for dr, dc, np in pipe[p]:
        flag = True
        for xr, xc in spaces[np]:
            nxr, nxc = r + xr, c + xc
            if 0 <= nxr < N and 0 <= nxc < N:
                if arr[nxr][nxc] == 1:
                    flag = False
                    break
        if flag:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
                # print(nr, nc)
                arr[nr][nc] = np
                dfs(nr, nc, np)
                arr[nr][nc] = 0


spaces = {
    'h': [[0, 1]],
    'v': [[1, 0]],
    'd': [[0, 1], [1, 0], [1, 1]],
}


pipe = {
    'h': [[0, 1, 'h'], [1, 1, 'd']],
    'v': [[1, 0, 'v'], [1, 1, 'd']],
    'd': [[0, 1, 'h'], [1, 0, 'v'], [1, 1, 'd']],
}


N = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
arr[0][0] = arr[0][1] = 'h'
cnt = 0
if arr[N-1][N-1] == 1:
    print(cnt)
else:
    dfs(0, 1, 'h')
    print(cnt)