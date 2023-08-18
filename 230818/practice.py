'''
7 8
1 2 1 3 2 4 2 5 4 
'''

def bfs(s, V): # 시작점 s, 마지막점 V
    # visited 생성
    vstd = [0] * (V+1)
    # 큐 생성
    Q = []
    # 시작점 인큐
    Q.append(s)
    # 시작점 방문표시
    vstd[s] = 1

    while Q: # 큐에 정점이 남아있으면 front != rear
        t = Q.pop()
        print(t) # 방문한 정점에서 할 일
        for w in adj_l[t]:
            if vstd[w] == 0:
                Q.append(w) # w 인큐, 방문 표시
                vstd[w] = vstd[t] + 1


V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append[v2]
    adj_l[v2].append[v1]

