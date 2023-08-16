import sys

sys.stdin = open("미로.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().strip() for _ in range(N)]

    s = [0, 0]
    e = [0, 0]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                s = [i, j]
            elif arr[i][j] == '3':
                e = [i, j]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    stack = []
    visited = [[False]*N for _ in range(N)]
    visited[s[0]][s[1]] = True
    flag = -1
    while flag == -1:
        block = 0
        for k in range(4):
            nr = s[0] + dr[k]
            nc = s[1] + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == '0' and visited[nr][nc] == False:
                    stack.append(s)
                    s = [nr, nc]
                    visited[nr][nc] = True
                elif arr[nr][nc] == '3':
                    s = [nr, nc]
                    flag = 1
                else:
                    block += 1
                    if block == 4:
                        if len(stack) == 0:
                            flag = 0
                        else:
                            s = stack.pop()
            else:
                block += 1
                if block == 4:
                    if len(stack) == 0:
                        flag = 0
                    else:
                        s = stack.pop()
    print(f"#{tc} {flag}")
