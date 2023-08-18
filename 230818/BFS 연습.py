import sys

sys.stdin = open("BFS 연습.txt", "r")

T = 1
for tc in range(1, T+1):

    # 노드와 간선의 개수
    V, E = map(int, input().split())

    # 간선에 대한 정보
    edge = list(map(int, input().split()))

    # 방문 표시 배열 생성
    vstd = [0]*(V+1)

    # 인접 매트릭스 생성
    adj_m = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        adj_m[edge[2*i]][edge[2*i+1]] = 1

    # 1부터 시작, BFS 탐색
    Q = [1]
    # 시작점에 방문 표시
    vstd[1] = 1
    # 방문점마다 표시하기 위한 배열
    trace = []
    # Q가 비지 않는 동안
    while Q:
        # 현재위치는 Q의 맨 앞
        pos = Q.pop(0)
        # 결과 배열에 현재 위치 저장
        trace.append(pos)
        for i in range(1, V+1):
            # 연결된(인접한) 노드인지, 그리고 방문한적 없는 노드인지 확인
            if adj_m[pos][i] == 1 and vstd[i] == 0:
                # 방문 표시 해주고
                vstd[i] = 1
                # 해당 노드를 Q에 대기시킴
                Q.append(i)

    print(f"#{tc}", *trace)
