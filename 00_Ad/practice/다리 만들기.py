import sys

sys.stdin = open('다리 만들기.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def mark_islands(number, r, c):
    for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            arr[nr][nc] = number
            mark_islands(number, nr, nc)


def combi(n, r, depth):
    if depth == r:
        return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
number = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] and visited[i][j] == 0:
            visited[i][j] = 1
            arr[i][j] = number
            mark_islands(number, i, j)
            number += 1
islands = [[] for _ in range(number + 1)]
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            islands[arr[i][j]].append((i, j))

used = [0] * number

# print(*islands, sep="\n")
# print(*arr, sep='\n')

min_d = float('inf')
for i in range(1, number):
    for j in range(i+1, number):
        for ar, ac in islands[i]:
            for br, bc in islands[j]:
                d = abs(ar-br)+abs(ac-bc)
                if min_d > d:
                    min_d = d
print(min_d-1)