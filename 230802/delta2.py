
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0             # 모든 원소가 0 이상이라면...
for i in range(N):
    for j in range(N):
        s = arr[i][j]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                s += arr[ni][nj]
        if max_v < s:
            max_v = s