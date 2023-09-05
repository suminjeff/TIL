import sys
import time
sys.stdin = open("나무 재테크.txt", "r")

start_time = time.time()


def spring():
    for r in range(N):
        for c in range(N):
            if age_list[r][c]:
                length = len(age_list[r][c])
                for i in range(length):
                    if age_list[r][c][i]:
                        if soil[r][c] - age_list[r][c][i] >= 0:
                            soil[r][c] -= age_list[r][c][i]
                            age_list[r][c][i] += 1
                        else:
                            age_list[r][c][i] = str(age_list[r][c][i])


def summer():
    for r in range(N):
        for c in range(N):
            if age_list[r][c]:
                length = len(age_list[r][c])
                for i in range(length):
                    if type(age_list[r][c][i]) == str:
                        soil[r][c] += int(age_list[r][c][i])//2
                        age_list[r][c][i] = 0


def fall():
    for r in range(N):
        for c in range(N):
            if age_list[r][c]:
                length = len(age_list[r][c])
                for i in range(length):
                    if age_list[r][c][i] > 0 and age_list[r][c][i] % 5 == 0:
                        for k in range(8):
                            nr = r + dr[k]
                            nc = c + dc[k]
                            if 0 <= nr < N and 0 <= nc < N:
                                age_list[nr][nc].append(1)
                                age_list[nr][nc].sort()


def winter():
    for r in range(N):
        for c in range(N):
            soil[r][c] += input_arr[r][c]


N, M, K = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range(N)]

soil = [[5]*N for _ in range(N)]
age_list = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    age_list[x-1][y-1].append(z)

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for year in range(K):
    spring()
    summer()
    fall()
    winter()

ans = 0
for r in range(N):
    for c in range(N):
        if age_list[r][c]:
            length = len(age_list[r][c])
            for i in range(length):
                if age_list[r][c][i] != 0:
                    ans += 1
print(ans)

end_time = time.time()
print("time :", end_time - start_time)