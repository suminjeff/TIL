import sys
sys.stdin = open("그래프 경로.txt", "r")


def dfs(n, V, adj_m):
    stack = []
    visited = [0] * (V+1)
    visited[n] = 1
    result = []
    while True:
        for w in range(1, V+1):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                result.append(n)
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return result


T = int(input())
for tc in range(1, T+1):
    # V = 노드 개수, E = 간선 개수
    V, E = map(int, input().split())

    # 빈 인접 매트릭스 생성
    adj_m = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        # 간선 정보 받기
        v1, v2 = map(int, input().split())

        # 인접 매트릭스 값 넣기
        adj_m[v1][v2] = 1

    # Start, Goal 지점
    S, G = map(int, input().split())

    ans = 0
    if G in dfs(S, V, adj_m):
        ans = 1

    print(f"#{tc} {ans}")

