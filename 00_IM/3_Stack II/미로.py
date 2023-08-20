import sys

sys.stdin = open("미로.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    # 시작점 찾기
    r = 0
    c = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r = i
                c = j
                break

    # DFS 탐색
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    visited = [[False]*N for _ in range(N)]
    stack = []
    visited[r][c] = True
    ans = -1
    while ans == -1:
        block = True
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] != 1 and visited[nr][nc] == False:
                    stack.append([r, c])
                    r, c = nr, nc
                    visited[r][c] = True
                    block = False
                    if arr[nr][nc] == 3:
                        ans = 1
                        break
        if block:
            if stack:
                r, c = stack.pop()
            else:
                ans = 0
    print(f"#{tc} {ans}")