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
    for j in range(M):
        v = arr[i][j]
        if v > 0:
            for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                    islands[v].append((i, j))
                    break

connected = [[0]*(number+1) for _ in range(number+1)]
ans = 0
for i in range(1, number+1):
    min_d = float('inf')
    connect = -1
    for r1, c1 in islands[i]:
        for j in range(1, number+1):
            if i != j and connected[i][j] == 0 and connected[j][i] == 0:
                for r2, c2 in islands[j]:
                    if r1 == r2 or c1 == c2:
                        d = abs(r1-r2) + abs(c1-c2) - 1
                        if min_d > d > 1:
                            min_d = d
                            connect = j
        if connect > 0:
            connected[i][connect] = 1
            connected[connect][i] = 1
            ans += min_d

print(*islands, sep='\n')
print(*arr, sep='\n')
print(ans)
