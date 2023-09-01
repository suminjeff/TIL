import sys

sys.stdin = open("탈주범 검거.txt", "r")


connected = {
    1: [[1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5], [1, 2, 5, 6]],
    2: [[], [1, 2, 4, 7], [], [1, 2, 5, 6]],
    3: [[1, 3, 6, 7], [], [1, 3, 4, 5], []],
    4: [[1, 3, 6, 7], [], [], [1, 2, 5, 6]],
    5: [[1, 3, 6, 7], [1, 2, 4, 7], [], []],
    6: [[], [1, 2, 4, 7], [1, 3, 4, 5], []],
    7: [[], [], [1, 3, 4, 5], [1, 2, 5, 6]],
}


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # i) 0 = right, 1 = down, 2 = left, 3 = up
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    que = [[R, C, L]]

    cnt = 0
    while que:
        r, c, t = que.pop(0)
        if t == 0:
            break
        else:
            if arr[r][c]:
                cnt += 1
                t -= 1
                shape1 = arr[r][c]
                arr[r][c] = 0
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        shape2 = arr[nr][nc]
                        if shape2:
                            if shape2 in connected[shape1][k]:
                                que.append([nr, nc, t])
            else:
                continue
    print(f"#{tc} {cnt}")