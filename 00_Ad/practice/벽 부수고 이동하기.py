import sys
sys.stdin = open("벽 부수고 이동하기.txt", "r")
input = sys.stdin.readline
import heapq
sys.setrecursionlimit(10**6)

def dfs(depth, smash, r, c):
    global min_distance
    visited[r][c] = 1
    if depth >= min_distance:
        return
    if smash > 1:
        return
    if r == N-1 and c == M-1:
        min_distance = min(min_distance, depth)
        return
    delta = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
    for nr, nc in delta:
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
            if arr[nr][nc] == "1":
                dfs(depth+1, smash+1, nr, nc)
            elif arr[nr][nc] == "0":
                dfs(depth+1, smash, nr, nc)
            visited[nr][nc] = 0


def bfs(heap):
    global min_distance
    while heap:
        distance, r, c, smashed = heapq.heappop(heap)
        visited[r][c] = 1
        if distance >= min_distance:
            continue
        if smashed > 1:
            continue
        if r == N-1 and c == M-1:
            min_distance = min(min_distance, distance)
            continue
        delta = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
        for nr, nc in delta:
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if arr[nr][nc] == "1":
                    heapq.heappush(heap, (distance+1, nr, nc, smashed+1))
                elif arr[nr][nc] == "0":
                    heapq.heappush(heap, (distance+1, nr, nc, smashed))

INF = float('inf')
N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
min_distance = INF


heap = []
heapq.heappush(heap, (1, 0, 0, 0))

dfs(1, 0, 0, 0)
# bfs(heap)
print(min_distance if min_distance != INF else -1)