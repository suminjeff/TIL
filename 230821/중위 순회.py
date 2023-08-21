import sys

sys.stdin = open("중위 순회.txt", "r")


def inorder(node):
    if node:
        inorder(c1[node])
        print(node_dict[node], end="")
        inorder(c2[node])
    else:
        return


T = 10
for tc in range(1, T+1):
    # 정점의 수
    N = int(input())
    node_dict = {}
    c1 = [0] * (N+1)
    c2 = [0] * (N+1)
    for i in range(N):
        edge = list(input().split())
        v, abc = int(edge.pop(0)), edge.pop(0)
        node_dict[v] = abc
        if edge:
            if len(edge) > 1:
                c1[v] = int(edge.pop(0))
                c2[v] = int(edge.pop(0))
            else:
                c1[v] = int(edge.pop(0))
    print(f"#{tc}", end=" ")
    inorder(1)
    print()
    # print(f"#{tc} {c1} {c2}")
    # print(f"#{tc} {adj_l}")