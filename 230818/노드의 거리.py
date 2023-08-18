import sys

sys.stdin = open("노드의 거리.txt", "r")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_l = [[] for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)
    S, G = map(int, input().split())
    vstd = [0]*(V+1)
    vstd[S] = 1

    queue = [S]

    ans = 0
    while queue:
        cur = queue.pop(0)
        for w in adj_l[cur]:
            if vstd[w] == 0:
                vstd[w] = vstd[cur] + 1
                if w == G:
                    ans = vstd[w] - 1
                    queue.clear()
                    break
                else:
                    queue.append(w)

    print(f"#{tc} {ans}")