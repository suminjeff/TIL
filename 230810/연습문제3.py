# 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열해 놓은 것
# 모든 정점을 깊이 우선 탐색해 화면에 깊이 우선 탐색 경로를 출력

'''
V E
v1 w1 v2 w2 ...
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(n, V, adj_m):
    stack = []                  # stack 생성
    visited = [0] * (V+1)       # visited 생성
    visited[n] = 1              # 시작점 방문 표시
    print(n)                    # do[n]
    while True:
        for w in range(1, V+1):   # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n) # push(v), v = w
                n = w           
                print(n)        # do(w)
                visited[n] = 1  # w 방문표시
                break           # for w, n에 인접인 w 찾은 경우
        else:
            if stack:           # 스택에 지나온 정점이 남아있으면
                n = stack.pop() # pop()해서 다시 다른 w를 찾을 n 준비
            else:               # 스택이 비어있으면
                break           # while True 탐색 종료


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adj_m = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1, V, adj_m)