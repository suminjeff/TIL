import sys
sys.stdin = open("빙산.txt", "r")
input = sys.stdin.readline
from collections import deque


def connected(r, c):
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = 1
            connected(nr, nc)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ice = deque()
water = [[0]*M for _ in range(N)]
K = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            K += 1
            ice.append((i, j, 0))
            for nr, nc in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                    water[i][j] += 1
year = 0
while K:
    # print("ICE")
    # print(*arr, sep="\n")
    # print("WATER")
    # print(*water, sep="\n")
    # print()
    # 연결 확인
    visited = [[0]*M for _ in range(N)]
    connected(ice[0][0], ice[0][1])
    isConnected = True
    for k in range(K):
        if visited[ice[k][0]][ice[k][1]] == 0:
            isConnected = False
            break
    if not isConnected:
        break
    else:
        melted = []
        # 녹이기
        for _ in range(K):
            r, c, y = ice.popleft()
            # 연도 업데이트
            if year < y:
                year = y
            v = arr[r][c] - water[r][c]
            arr[r][c] = v if v > 0 else 0
            if arr[r][c]:
                ice.append((r, c, y+1))
            else:
                K -= 1
                melted.append((r, c))
        # 바다 정보 업데이트
        for mr, mc in melted:
            water[mr][mc] = 0
            for nmr, nmc in [[mr+1, mc], [mr-1, mc], [mr, mc+1], [mr, mc-1]]:
                if 0 <= nmr < N and 0 <= nmc < M and arr[nmr][nmc] > 0:
                    water[nmr][nmc] += 1

print(year)