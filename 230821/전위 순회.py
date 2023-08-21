import sys

sys.stdin = open("전위 순회.txt", "r")


def preorder(node):
    global V
    if node:
        print(node, end=" ")
        if node != V:
            preorder(c1[node])
            preorder(c2[node])

V = int(input())
edge = list(map(int, input().split()))

c1 = [0] * (V+1)
c2 = [0] * (V+1)

for i in range(len(edge)//2):
    f, s = edge[2*i], edge[2*i+1]
    if c1[f] == 0:
        c1[f] = s
    else:
        c2[f] = s
preorder(1)
