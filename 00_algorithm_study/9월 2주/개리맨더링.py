import sys

sys.stdin = open("개리맨더링.txt", "r")

import time
start_time = time.time()


def dfs(v, adj_l, vstd, division):
    vstd[v] = 1
    for i in adj_l[v]:
        if i in division:
            dfs(i, adj_l, vstd)
        else:
            continue


def get_div2(div1, total):
    div2 = []
    for x in total:
        if x not in div1:
            div2.append(x)
    return div2


def subsets(city_n):
    subset_list = []
    for i in range(1 << city_n):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(j)
        if 0 < len(subset) <= city_n//2:
            subset_list.append(subset)
    return subset_list


N = int(input())
cities = [n for n in range(N)]
population = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    length = graph[i].pop(0)
    for j in range(length):
        graph[i][j] -= 1
division1 = subsets(N)
division2 = []
for d1 in division1:
    division2.append(get_div2(d1, cities))
for d1 in division1:



end_time = time.time()
print(end_time - start_time)