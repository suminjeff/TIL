import sys

sys.stdin = open("subtree.txt", "r")


def subtree(v):
    global cnt
    if v:
        cnt += 1
        subtree(c1[v])
        subtree(c2[v])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))
    c1 = [0] * (E+2)
    c2 = [0] * (E+2)
    for i in range(len(edge)//2):
        v1, v2 = edge[2*i], edge[2*i+1]
        if c1[v1]:
            c2[v1] = v2
        else:
            c1[v1] = v2
        p[v2] = v1
    cnt = 0
    subtree(N)
    print(f"#{tc} {cnt}")