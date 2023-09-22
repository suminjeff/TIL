import sys
sys.stdin = open("창용 마을 무리의 개수.txt", "r")
input = sys.stdin.readline


def dfs(person, isGroup):
    global cnt
    visited[person] = 1
    if adj_l[person]:
        for next_person in adj_l[person]:
            if not visited[next_person]:
                dfs(next_person, True)
        if not isGroup:
            cnt += 1
    else:
        cnt += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_l = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    for _ in range(M):
        f, t = map(int, input().split())
        adj_l[f].append(t)
        adj_l[t].append(f)
    cnt = 0
    for starting_person in range(1, N+1):
        if not visited[starting_person]:
            dfs(starting_person, False)
    print(f"#{tc} {cnt}")