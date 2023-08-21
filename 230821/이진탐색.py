import sys

sys.stdin = open("이진탐색.txt", "r")


def inorder(node):
    global N
    global v
    if node <= N:
        inorder(2*node)
        tree[node] = v
        v += 1
        inorder(2*node+1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 트리 만들기
    tree = [0] * (N+1)
    v = 1
    inorder(1)
    print(f"#{tc} {tree[1]} {tree[N//2]}")

    #
    # v = 1
    # # 트리의 레벨 구하기
    # level = 0
    # while True:
    #     if 2 ** level <= N < 2 ** (level + 1):
    #         break
    #     else:
    #         level += 1
    #
    # # 트리 만들기
    # tree = [[] for _ in range(2**level)]
    # child = 2
    # parent = 1
    # while child <= N:
    #     if len(tree[parent]) >= 2:
    #         parent += 1
    #     tree[parent].append(child)
    #     child += 1
    #
    # tree_dict = {}
    # print(tree_dict)