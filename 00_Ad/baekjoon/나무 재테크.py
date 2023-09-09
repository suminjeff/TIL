import sys
import time
sys.stdin = open("나무 재테크.txt", "r")
start_time = time.time()

N, M, K = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range(N)]

soil = [[5]*N for _ in range(N)]
trees = []
for _ in range(M):
    x, y, z = map(int, input().split())
    trees.append([x-1, y-1, z])
start_i = 0
end_i = M
dead = []

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]


for year in range(K):
    # spring
    trees.sort(key=lambda x: x[2])
    spr_length = len(trees)
    for i in range(spr_length):
        spr_r, spr_c, spr_age = trees.pop(0)
        if soil[spr_r][spr_c] >= spr_age:
            soil[spr_r][spr_c] -= spr_age
            trees.append([spr_r, spr_c, spr_age+1])
        else:
            dead.append([spr_r, spr_c, spr_age])

    # summer
    if dead:
        while dead:
            sum_r, sum_c, dead_age = dead.pop()
            soil[sum_r][sum_c] += dead_age//2

    # fall
    fall_length = len(trees)
    for j in range(fall_length):
        fall_r, fall_c, fall_age = trees[j]
        if fall_age % 5 == 0:
            for k in range(8):
                nr = fall_r + dr[k]
                nc = fall_c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    trees.append([nr, nc, 1])
                    end_i += 1

    # winter
    for win_r in range(N):
        for win_c in range(N):
            soil[win_r][win_c] += input_arr[win_r][win_c]

print(len(trees))


end_time = time.time()
print("time :", end_time - start_time)