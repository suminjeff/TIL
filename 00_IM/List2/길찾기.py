
# n = 시작점, V = 분기점의 개수, adj_m = 인접 매트릭스
def dfs(n, V, adj_m):
    # stack 배열 생성
    stack = []

    # visited 배열 생성 (V+1개), 시작점은 방문 표시
    visited = [0] * (V+1)
    visited[n] = 1

    # 경로 히스토리
    result = [n]

    #
    while True:
        # 시작점을 제외한 V-1개 분기점에 대해 탐색
        for w in range(1, V):
            # 인접 매트릭스에서 n(출발점)과 w(도착점)가 인접해있는지 확인하고, w의 방문 표시가 없는 것을 확인
            if adj_m[n][w] == 1 and visited[w] == 0:
                # stack에 n을 추가
                stack.append(n)

                # n을 w로 갱신
                n = w

                # 결과에 n 추가
                result.append(n)

                # 갱신된 n에 방문 표시
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return result


T = 10
for _ in range(1, T+1):
    tc, E = map(int, input().split())
    edge = list(map(int, input().split()))
    adj_m = [[0]*100 for _ in range(100)]
    for i in range(E):
        v1, v2 = edge[i*2], edge[i*2+1]
        adj_m[v1][v2] = 1
    ans = 0
    if 99 in dfs(0, 10, adj_m):
        ans = 1
    print(f"#{tc} {ans}")