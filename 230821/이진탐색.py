import sys

sys.stdin = open("이진탐색.txt", "r")


def inorder(node):
    if node:
        inorder(tree[node])
        print(node)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    v = 1
    # 트리의 레벨 구하기
    level = 0
    while True:
        if 2 ** level <= N < 2 ** (level + 1):
            break
        else:
            level += 1

    # 트리 만들기
    tree = [[] for _ in range(2**level)]
    child = 2
    parent = 1
    while child <= N:
        if len(tree[parent]) >= 2:
            parent += 1
        tree[parent].append(child)
        child += 1

    tree_dict = {}
    inorder(1)

    print(tree_dict)
    print(level)
