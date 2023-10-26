import sys
sys.stdin = open('미세먼지 안녕!.txt', 'r')
input = sys.stdin.readline

from collections import deque

# 1. 미세먼지 확산 (상하좌우로 //5씩 확산)
#     a. 인접한 방향으로 확산
#     b. 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산x
#     c. (r, c)에 남은 미세먼지 양은 A - (A//5)*(확산된 방향의 개수)
# 2. 공기청정기 작동 (위쪽은 반시계, 아래쪽은 시계 방향)
#     a. 바람 방향대로 한칸씩 이동
#     b. 공기청정기로 먼지가 들어가면 정화


def dust(dust_que):
    global dust_pos_N
    global total_dust
    dust_pos = {}
    for _ in range(dust_pos_N):
        r, c = dust_que.popleft()
        v = arr[r][c]
        if (r, c) not in dust_pos:
            dust_pos.setdefault((r, c), 0)
        dust_pos[(r, c)] += v
        w = v//5
        if w > 0:
            cnt = 0
            for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                    cnt += 1
                    if (nr, nc) not in dust_pos:
                        dust_pos.setdefault((nr, nc), 0)
                    dust_pos[(nr, nc)] += w
            dust_pos[(r, c)] -= w*cnt
    new_dust_pos_N = 0
    new_total_dust = 0
    for k, v in dust_pos.items():
        nr, nc = k
        if v > 0:
            arr[nr][nc] = v
            dust_que.append([nr, nc])
            new_dust_pos_N += 1
            new_total_dust += v
    dust_pos_N = new_dust_pos_N
    total_dust = new_total_dust


def air_cleaner(ac, dust_que):
    global dust_pos_N
    global total_dust
    dust_pos = {}
    upper, lower = ac[0], ac[1]
    for _ in range(dust_pos_N):
        r, c = dust_que.popleft()
        v = arr[r][c]

        # 반시계
        # idx = 0
        if r <= upper:
            if r == upper or r == 0 or c == 0 or c == C-1:
                arr[r][c] = 0
                if r == upper and 0 <= c < C-1:
                    idx = 0
                elif r == 0 and 0 < c <= C-1:
                    idx = 2
                elif c == 0 and 0 <= r < upper:
                    idx = 1
                elif c == C-1 and 0 < r <= upper:
                    idx = 3
                nr, nc = r + clockwise[idx][0], c + clockwise[idx][1]
                if 0 <= nr < R and 0 <= nc < C:
                    if arr[nr][nc] != -1:
                        if (nr, nc) not in dust_pos:
                            dust_pos.setdefault((nr, nc), 0)
                        dust_pos[(nr, nc)] += v
                    else:
                        total_dust -= v
            else:
                if (r, c) not in dust_pos:
                    dust_pos.setdefault((r, c), 0)
                dust_pos[(r, c)] += v

        # 시계
        elif r >= lower:
            if r == lower or r == R-1 or c == 0 or c == C-1:
                v = arr[r][c]
                arr[r][c] = 0
                if r == lower and 0 <= c < C-1:
                    idx = 0
                elif r == R-1 and 0 < c <= C-1:
                    idx = 2
                elif c == 0 and upper < r <= R-1:
                    idx = 3
                elif c == C-1 and upper <= r < R-1:
                    idx = 1
                nr, nc = r + clockwise[idx][0], c + clockwise[idx][1]
                if 0 <= nr < R and 0 <= nc < C:
                    if arr[nr][nc] != -1:
                        if (nr, nc) not in dust_pos:
                            dust_pos.setdefault((nr, nc), 0)
                        dust_pos[(nr, nc)] += v
                    elif arr[nr][nc] == -1:
                        total_dust -= v
            else:
                if (r, c) not in dust_pos:
                    dust_pos.setdefault((r, c), 0)
                dust_pos[(r, c)] += v

    new_dust_pos_N = 0
    for k, v in dust_pos.items():
        nr, nc = k
        arr[nr][nc] = v
        dust_que.append([nr, nc])
        new_dust_pos_N += 1
    dust_pos_N = new_dust_pos_N


# 우 하 좌 상
clockwise = [[0, 1], [1, 0], [0, -1], [-1, 0]]
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
dust_que = deque()
dust_pos_N = 0
total_dust = 0
ac = []
for r in range(R):
    if arr[r][0] == -1:
        ac.append(r)
    for c in range(C):
        v = arr[r][c]
        if v > 0:
            dust_que.append([r, c])
            dust_pos_N += 1
            total_dust += v

for t in range(T):
    dust(dust_que)
    air_cleaner(ac, dust_que)
print(total_dust)