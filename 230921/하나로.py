import sys
sys.stdin = open("하나로.txt", "r")
input = sys.stdin.readline

import heapq


def prim(start):
    heap = []
    # MST 에 포함되었는 지 여부
    MST = [0] * N

    # 가중치, 정점 정보
    heapq.heappush(heap, (0, start))
    # 누적합 저장
    sum_weight = 0

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)

        # 이미 방문한 노드라면 pass
        if MST[v]:
            continue

        # 방문 체크
        MST[v] = 1

        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 체크
        for next in range(N):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    # 인접행렬
    graph = [[0] * N for _ in range(N)]
    for i1 in range(N):
        for i2 in range(N):
            if i1 != i2:
                graph[i1][i2] = E * ((X[i1]-X[i2])**2 + (Y[i1]-Y[i2])**2)

    result = round(prim(0))
    print(f'#{tc} {result}')


