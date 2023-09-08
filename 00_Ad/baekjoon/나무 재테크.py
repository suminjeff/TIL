import sys
import time
sys.stdin = open("나무 재테크.txt", "r")

start_time = time.time()


N, M, K = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range(N)]

soil = [[5]*N for _ in range(N)]
trees = []
front = rear = -1
year = 0

for _ in range(M):
    x, y, z = map(int, input().split())
    trees.append((x-1, y-1, [z], []))
    rear += 1

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for year in range(K):
    # spring
    for tree in trees:
        r, c, age_list, dead = tree
        front += 1
        age_list.sort()
        for i in range(len(age_list)):
            if age_list[i]:
                if soil[r][c] - age_list[i] >= 0:
                    soil[r][c] -= age_list[i]
                    age_list[i] += 1
                else:
                    dead.append(str(age_list[i]))
                    age_list[i] = 0
        trees.append((r, c, age_list, dead))
        rear += 1

    # summer
    for tree in trees:
        r, c, age_list, dead = tree
        for dead_tree in dead:
            for k in range(8):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:






print(input_arr)
print(soil)
print(trees)
print(age_list)

end_time = time.time()
print("time :", end_time - start_time)