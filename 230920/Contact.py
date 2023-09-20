'''
#1 17
#2 96
#3 49
#4 39
#5 49 x
#6 1 x
#7 28
#8 45
#9 59
#10 64
'''


import sys
sys.stdin = open("Contact.txt", "r")


def bfs(que):
    while que:
        v, degree = que.pop(0)
        degree += 1
        if adj_l[v]:
            for w in adj_l[v]:
                if not visited[w]:
                    visited[w] = degree
                    que.append([w, degree])


T = 10
for tc in range(1, T + 1):
    N, v = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_l = [[] for _ in range(101)]
    visited = [0] * 101
    for i in range(N // 2):
        adj_l[arr[2 * i]].append(arr[2 * i + 1])
    que = [[v, 1]]
    visited[v] = 1
    bfs(que)
    max_degree = max(visited)
    ans = 0
    for j in range(100, -1, -1):
        if visited[j] == max_degree:
            ans = j
            break
    print(f"#{tc} {ans}")