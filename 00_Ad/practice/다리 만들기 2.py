import sys
sys.stdin = open('다리 만들기 2.txt', 'r')
input = sys.stdin.readline


def mark_islands(number, r, c):
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            arr[nr][nc] = number
            mark_islands(number, nr, nc)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
number = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] and visited[i][j] == 0:
            visited[i][j] = 1
            arr[i][j] = number
            mark_islands(number, i, j)
            number += 1

islands = [[] for _ in range(number + 1)]
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            islands[arr[i][j]].append((i, j))


print(*arr, sep='\n')

