import sys
sys.stdin = open('내리막 길.txt', 'r')
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def dfs(r, c):
    global ans
    if (r, c) == (M-1, N-1):
        ans += 1
        return
    for nr, nc in [[r-1, c], [r, c+1], [r, c-1], [r+1, c]]:
        if 0 <= nr < M and 0 <= nc < N and arr[r][c] > arr[nr][nc] and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(nr, nc)
            visited[nr][nc] = 0


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
visited[0][0] = 1
ans = 0
dfs(0, 0)
print(ans)