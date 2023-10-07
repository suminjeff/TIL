import sys
sys.stdin = open("캐슬 디펜스.txt", "r")
input = sys.stdin.readline
from collections import deque

def nCr(n, r, res):
    global max_cnt
    if n == len(position):
        if len(res) == r:
            cnt = shoot(res)
            print(cnt)
            print()
            max_cnt = max(max_cnt, cnt)
        return
    res.append(position[n])
    nCr(n+1, r, res)
    res.pop()
    nCr(n+1, r, res)


def shoot(archer_position):
    a1, a2, a3 = archer_position
    kill_cnt = 0
    killed = [[0]*M for _ in range(N)]
    wave = N-1
    for r in range(wave, -1, -1):
        visited = [[0]*M for _ in range(N)]
        for c in archer_position:
            t = target(c, r, D, killed, visited)
            print(t, c)
            if t:
                killed[t][c] = 1
                kill_cnt += 1
    return kill_cnt


def target(archer, wave, shot_range, killed, visited):
    que = deque()
    que.append([archer, wave+1, 1])
    while que:
        c, r, s = que.popleft()
        if s > shot_range:
            break
        s += 1
        for dr, dc in shooting_direction:
            nr, nc = r + dr, c + dc
            if 0 <= nr < wave+1 and 0 <= nc < wave+1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if enemy[nr][nc] == 1 and killed[nr][nc] == 0:
                    return nr
                que.append([nc, nr, s])



shooting_direction = [[0, -1], [-1, 0], [0, -1]]

N, M, D = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(N)] + [[2]*M]
position = [m for m in range(M)]
archers = [0] * 3
max_cnt = 0
nCr(0, 3, [])