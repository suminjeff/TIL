import sys

sys.stdin = open("노드의 합.txt", "r")


T = int(input())
for tc in range(1, T+1):
    # N = 노드의 개수, M = 리프 노드의 개수, L = 출력할 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        node, v = map(int, input().split())
        tree[node] = v

    for i in range(N//2, 0, -1):
        c1, c2 = 2*i, 2*i+1
        if c2 <= N:
            tree[i] = tree[c1] + tree[c2]
        elif c1 <= N:
            tree[i] = tree[c1]
    print(f"#{tc} {tree[L]}")