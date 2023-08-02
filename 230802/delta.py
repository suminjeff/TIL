# N = 2
# M = 4
# arr = [[0, 1, 2, 3,], [4, 5, 6, 7]]
# for i in range(M):
#     for j in range(N):
#         print(arr[j][i])

# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# max_v = 0             # 모든 원소가 0 이상이라면...
# for i in range(N):
#     for j in range(N):
#         s = arr[i][j]
#         for k in range(4):
#             ni, nj = i+di[k], j+dj[k]
#             if 0<=ni<N and 0<=nj<N:
#                 s += arr[ni][nj]
#         if max_v < s:
#             max_v = s


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0             # 모든 원소가 0 이상이라면...
for i in range(N):
    for j in range(N):
        s = arr[i][j]
        for k in range(4):
            for p in range(1, m):
                ni, nj = i+di[k]*p, j+dj[k]*p
                if 0<=ni<N and 0<=nj<N:
                    s += arr[ni][nj]
            if max_v < s:
                max_v = s