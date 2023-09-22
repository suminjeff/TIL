import sys
sys.stdin = open("최소 비용.txt", "r")
input = sys.stdin.readline

import heapq

inf = int(1e9)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cost = [[inf]*N for _ in range(N)]
    start_r = start_c = 0
    cost[start_r][start_c] = 0
    pq = []
    heapq.heappush(pq, (cost[start_r][start_c], start_r, start_c))
    while pq:
        print("pop", pq)
        w, r, c = heapq.heappop(pq)
        if cost[r][c] >= w:
            cost[r][c] = w
            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < N:
                    nw = cost[r][c] + 1
                    if arr[nr][nc] > arr[r][c]:
                        nw += arr[nr][nc] - arr[r][c]
                    if cost[nr][nc] > nw:
                        cost[nr][nc] = nw
                        heapq.heappush(pq, (nw, nr, nc))
                        print("push", pq)
    print(f"#{tc} {cost[N-1][N-1]}")
