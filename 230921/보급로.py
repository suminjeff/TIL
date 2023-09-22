import sys
sys.stdin = open("보급로.txt", "r")
input = sys.stdin.readline
import heapq

inf = int(1e9)

def dijkstra(w, i, j):
    pq = []
    heapq.heappush(pq, (w, i, j))
    time[i][j] = 0
    while pq:
        w, i, j = heapq.heappop(pq)
        w += arr[i][j]
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                if time[ni][nj] > w:
                    time[ni][nj] = w
                    heapq.heappush(pq, (time[ni][nj], ni, nj))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().rstrip()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = int(arr[i][j])
    time = [[inf]*N for _ in range(N)]
    dijkstra(0, 0, 0)
    ans = time[N-1][N-1]
    print(f"#{tc} {ans}")