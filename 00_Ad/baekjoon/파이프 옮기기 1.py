import sys
sys.stdin = open('파이프 옮기기 1.txt', 'r')
input = sys.stdin.readline


# def dfs(r, c, p):
#     global cnt
#     if r == c == N-1:
#         cnt += 1
#         return
#
#     for dr, dc, np in pipe[p]:
#         nr, nc = r + dr, c + dc
#         if np == 'd':
#             if nr < N and nc < N and arr[nr][nc] == arr[nr-1][nc] == arr[nr][nc-1] == 0:
#                 dfs(nr, nc, np)
#         else:
#             if nr < N and nc < N and arr[nr][nc] == 0:
#                 dfs(nr, nc, np)
#
# pipe = {
#     'h': [[0, 1, 'h'], [1, 1, 'd']],
#     'v': [[1, 0, 'v'], [1, 1, 'd']],
#     'd': [[0, 1, 'h'], [1, 0, 'v'], [1, 1, 'd']],
# }
#
#
# N = int(input())
# arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
# cnt = 0
#
# if arr[N-1][N-1] == 1:
#     print(cnt)
# else:
#     dfs(0, 1, 'h')
#     print(cnt)
#


def dfs(r, c, p):
    print(r, c, memo[r][c])
    if r == c == N-1:
        return 1
    if memo[r][c][p] != -1:
        return memo[r][c][p]
    total_cnt = 0
    for dr, dc, np in pipe[p]:
        nr, nc = r + dr, c + dc
        if np == 2:
            if nr < N and nc < N and arr[nr][nc] == arr[nr-1][nc] == arr[nr][nc-1] == 0:
                total_cnt += dfs(nr, nc, np)
        else:
            if nr < N and nc < N and arr[nr][nc] == 0:
                total_cnt += dfs(nr, nc, np)
    memo[r][c][p] = total_cnt
    return total_cnt


pipe = {
    0: [[0, 1, 0], [1, 1, 2]],
    1: [[1, 0, 1], [1, 1, 2]],
    2: [[0, 1, 0], [1, 0, 1], [1, 1, 2]],
}

N = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
memo = [[[-1 for _ in range(3)] for _ in range(N)] for _ in range(N)]
result = dfs(0, 1, 0)

print(result)
