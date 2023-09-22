import sys
sys.stdin = open("최소 이동 거리.txt", "r")
input = sys.stdin.readline

inf = int(1e9)


def get_smallest_node():
    min_value = inf
    idx = 0
    for i in range(1, N + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx


def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(N - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    distance = [inf] * (N+1)
    visited = [False] * (N+1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
    start = 0
    dijkstra(start)

    print(f"#{tc} {distance[N]}")