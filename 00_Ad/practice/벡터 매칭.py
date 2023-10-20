import sys
sys.stdin = open('벡터 매칭.txt', 'r')
input = sys.stdin.readline
from math import sqrt


def backtrack(depth, pair, x_vector, y_vector):
    # 일단 값이 최소값보다 크면 끝내기
    global min_v
    # if min_v <= v:
    #     return

    # 짝이 다 정해지면 최소값 갱신해주기
    if depth == N//2:
        v = sqrt(x_vector**2 + y_vector**2)
        if min_v > v:
            min_v = v
        return

    # pair가 2명이면 clear
    if len(pair) == 2:
        depth += 1
        x_vector += distance[pair[0]][pair[1]][0]
        y_vector += distance[pair[0]][pair[1]][1]
        pair.clear()
    # pair가 0~1명이면 한명 뽑기
    elif len(pair) < 2:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                pair.append(i)
                backtrack(depth, pair, x_vector, y_vector)
                visited[i] = 0




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    distance = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = P[i]
            x2, y2 = P[j]
            vector1 = [x1-x2, y1-y2]
            vector2 = [x2-x1, y2-y1]
            distance[i][j] = vector1
            distance[j][i] = vector2

    min_v = float('inf')
    visited = [0]*N
    for i in range(N):
        visited[i] = 1
        backtrack(1, [i], 0, 0)
        visited[i] = 0
    print(*distance, sep="\n")
    print(min_v)