import sys

sys.stdin = open("Contact.txt", "r")

T = 10

for tc in range(1, T+1):
    # 인접리스트, visited 초기 설정
    MAXCAP = 100
    # adj_l = [set() for _ in range(MAXCAP+1)]
    adj_m = [[0] * (MAXCAP+1) for _ in range(MAXCAP+1)]
    vstd = [0] * (MAXCAP+1)

    # 입력1 : 데이터의 크기 N, 시작점 S
    N, S = map(int, input().split())
    # 입력2 : 간선 정보 (누가 누구랑 연결되어 있는지)
    edge = list(map(int, input().split()))
    for i in range(N//2):
        # adj_l[edge[2*i]].add(edge[2*i+1])
        adj_m[edge[2*i]][edge[2*i+1]] = 1
    queue = [S]
    vstd[S] = 1
    while queue:
        cur = queue.pop(0)
        for w in range(101):
            if vstd[w] == 0 and adj_m[cur][w] == 1:
                vstd[w] = vstd[cur] + 1
                queue.append(w)
    max_v = max(vstd)
    ans = 0
    for i in edge:
        if vstd[i] == max_v:
            if ans < i:
                ans = i
    print(f"#{tc} {ans}")