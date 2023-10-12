import sys
sys.stdin = open('최단경로.txt', 'r')
input = sys.stdin.readline
import heapq


INF = float('inf')

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, now = heapq.heappop(heap)
        if distance[now] < weight:
            continue
        for w, next in graph[now]:
            nw = weight + w
            if nw < distance[next]:
                distance[next] = nw
                heapq.heappush(heap, (nw, next))


def backtrack(depth, d, s):
    global min_distance
    if depth == V:
        min_distance = min(min_distance, d)
        return
    if d >= min_distance:
        return
    for w, e in graph[s]:
        distance[e] = min(distance[e], d+w)
        backtrack(depth+1, d+w, e)


V, E = map(int, input().split())
S = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)
heap = []

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])
dijkstra(S)

for i in range(1, V+1):
    if distance[i] == INF:
        distance[i] = "INF"
    print(distance[i])
