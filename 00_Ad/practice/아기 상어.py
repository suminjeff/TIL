import sys
sys.stdin = open('아기 상어.txt', 'r')
input = sys.stdin.readline

from collections import deque


def find_candidates(r, c, bs_size, fish_pos):

    for i in range(1, bs_size):
        for fr, fc in fish_pos[i]:



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 9: 아기상어의 위치
# 1~6: 물고기의 크기
# 이동 조건
# 1. 자신보다 크기가 큰 물고기가 있는 칸은 지날 수 없고 나머지 (같거나 작은) 칸은 모두 지날 수 있음
# 2. 자신보다 크기가 작은 물고기만 먹을 수 있음
# 이동 방법
#     a) 더 이상 먹을 수 있는 물고기가 없다면 어미 상어에게 도움을 청한다.
#     b) 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 간다.
#     c) 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운(지나야하는 칸의 개수의 최솟값) 물고기를 먹으러 간다.
#         i. 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 떄, 지나야하는 칸의 개수의 최솟값
#        ii. 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다
# 2. 이동은 1초 걸리고, 물고기를 먹는 데에 걸리는 시간은 없다고 가정 (즉, 이동 즉시 먹음)
#     - 물고기를 먹으면 그 칸은 빈 칸이 됨
# 3. 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
# 문제 : 아기 상어가 몇 초 동안 엄마 상어에게 도움을 청하지 않고 물고기를 잡아먹을 수 있는지 구하기

# 아기 상어의 위치와 먹을 수 있는 물고기의 개수 세기
# fish_N = 먹을 수 있는 물고기
bs_size = 2
bs_pos = []
f_pos = [[] for _ in range(7)]
candidates = []
for i in range(N):
    for j in range(N):
        v = arr[i][j]
        if 1 <= v <= 6:
            f_pos[v].append([i, j])
            if v < bs_size:
                candidates.append([i, j])
        elif v == 9:
            bs_pos = [i, j]
for i in range(1, 7):
    f_pos[i].sort(key=lambda x:(x[0], x[1]))





# 먹을 수 있는 물고기가 있는 동안 반복 (엄마 상어에게 도움을 청하기 직전까지)
# T = 지난 시간


print(f_pos)