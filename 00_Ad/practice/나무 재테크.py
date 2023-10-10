import sys
import time
sys.stdin = open("나무 재테크.txt", "r")
start_time = time.time()


def spring_summer():
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                trees[r][c].sort()
                temp = []
                dead = 0
                for age in trees[r][c]:
                    if soil[r][c] >= age:
                        soil[r][c] -= age
                        temp.append(age+1)
                        if (age+1) % 5 == 0:
                            parents.append([r, c])
                    else:
                        dead += age//2
                trees[r][c] = temp
                soil[r][c] += dead


def fall(parent):
    r, c = parent
    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            trees[nr][nc].append(1)


def winter():
    for r in range(N):
        for c in range(N):
            soil[r][c] += input_arr[r][c]


def count_trees():
    ans = 0
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                ans += len(trees[i][j])
    return ans


N, M, K = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range(N)]

soil = [[5]*N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for year in range(1, K+1):
    parents = []
    spring_summer()
    if parents:
        for parent in parents:
            fall(parent)
        parents.clear()
    winter()
print(count_trees())

end_time = time.time()
print("time :", end_time - start_time)