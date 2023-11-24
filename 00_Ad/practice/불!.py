import sys
sys.stdin = open('불!.txt', 'r')
input = sys.stdin.readline

from collections import deque

R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]
ji = deque()
visited = [[0]*C for _ in range(R)]
fire = deque()
fire_visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            visited[i][j] = 1
            ji.append([i, j])
        elif arr[i][j] == 'F':
            fire_visited[i][j] = 1
            fire.append([i, j])
ans = -1

while fire:
    r, c = fire.popleft()
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < R and 0 <= nc < C and fire_visited[nr][nc] == 0:
            fire_visited[nr][nc] = fire_visited[r][c] + 1
            fire.append([nr, nc])
print(*fire_visited, sep='\n')
ans = "IMPOSSIBLE"
while ji:
    r, c = ji.popleft()
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] in ".J" and visited[nr][nc] == 0:
            if 1 <= nr < R-1 and 1 <= nc < C-1:
                if fire_visited[nr][nc] > visited[r][c]+1:
                    visited[nr][nc] = visited[r][c] + 1
                    ji.append([nr, nc])
            else:
                visited[nr][nc] = visited[r][c]+1
                ans = visited[nr][nc]
    if ans != "IMPOSSIBLE":
        break
print()
print(*visited, sep='\n')
print(ans)

# while ji:
#     t, r, c = ji.popleft()
#     fN = len(fire)
#     for _ in range(fN):
#         fr, fc = fire.popleft()
#         for nfr, nfc in [[fr+1, fc], [fr-1, fc], [fr, fc+1], [fr, fc-1]]:
#             if 0 <= nfr < R and 0 <= nfc < C and arr[nfr][nfc] == '.' and fire_visited[nfr][nfc] == 0:
#                 fire_visited[nfr][nfc] = 1
#                 fire.append([nfr, nfc])
#     flag = False
#     for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
#         if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == '.' and fire_visited[nr][nc] == 0 and visited[nr][nc] == 0:
#             visited[nr][nc] = 1
#             ji.append([t+1, nr, nc])
#         elif nr < 0 or nr >= R or nc < 0 or nc >= C:
#             flag = True
#             ans = t+1
#             break
#     if flag:
#         break
# if ans == -1:
#     print('IMPOSSIBLE')
# else:
#     print(ans)