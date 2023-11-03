import sys
sys.stdin = open('친구 네트워크.txt', 'r')
input = sys.stdin.readline


def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)
    children[min(x, y)] += 1
    children[min(x, y)] += children[max(x, y)]
    children[max(x, y)] = 0


T = int(input())
for tc in range(1, T+1):
    auto_increment = 0
    F = int(input())
    adj_l = [[] for _ in range(100002)]
    parents = [i for i in range(100002)]
    children = [0]*100002
    pk = {}
    for _ in range(F):
        p1, p2 = input().split()
        if p1 not in pk.keys():
            pk.setdefault(p1, auto_increment)
            auto_increment += 1
        if p2 not in pk.keys():
            pk.setdefault(p2, auto_increment)
            auto_increment += 1
        adj_l[pk[p1]].append(pk[p2])
        adj_l[pk[p2]].append(pk[p1])
        union(pk[p1], pk[p2])
        print(children[parents[pk[p1]]]+1)

