import sys
sys.stdin = open("인수의 생일파티.txt", "r")
input = sys.stdin.readline

import heapq
inf = int(1e9)


def dijkstra(start):
    pq = []
    # 시작 노드로 가기 위한 최단 경로는 0
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pq, (cost, i[0]))


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append([y, c])

    X_to_others = []
    others_to_X = [[] for _ in range(N+1)]

    for start_node in range(1, N+1):
        distance = [inf] * (N+1)
        if start_node != X:
            dijkstra(start_node)
            others_to_X[start_node] = distance
        else:
            dijkstra(X)
            X_to_others = distance
    max_dist = 0
    for i in range(1, N+1):
        if i != X:
            max_dist = max(max_dist, X_to_others[i] + others_to_X[i][X])
    print(f"#{tc} {max_dist}")