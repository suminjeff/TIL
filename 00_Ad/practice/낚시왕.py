import sys
sys.stdin = open('낚시왕.txt', 'r')
input = sys.stdin.readline
from collections import deque


def catch(k):
    global M
    for row in range(R):
        if sharks[row][k]:
            for i in range(M):
                r, c, s, d, z = que[i]
                if row == r and k == c:
                    que.remove(que[i])
                    M -= 1
                    break
            v = sharks[row][k]
            sharks[row][k] = 0
            return v
    return 0


def shark_move(que):
    global M
    shark_pos = {}
    for m in range(M):
        r, c, s, d, z = que.popleft()
        sharks[r][c] = 0
        nr = nc = -1
        # 1: 상, 2: 하
        if d == 1 or d == 2:
            nc = c
            # 위
            if d == 1:
                rs = r-s
                # 방향
                if 0 < rs % (2*(R-1)) <= R-1:
                    d = d
                else:
                    d = 3 - d
            # 아래
            else:
                rs = r+s
                if 0 < rs % (2*(R-1)) <= R-1:
                    d = d
                else:
                    d = 3 - d
            # 위치
            if rs % (2*(R-1)) <= R-1:
                nr = rs % (2*(R-1))
            else:
                nr = 2*(R-1) - rs % (2*(R-1))

        # 3: 우, 4: 좌
        elif d == 3 or d == 4:
            nr = r
            # 왼쪽
            if d == 4:
                cs = c-s
                if 0 < cs % (2*(C-1)) <= C-1:
                    d = d
                else:
                    d = 7 - d
            # 오른쪽
            else:
                cs = c+s
                if 0 < cs % (2*(C-1)) <= C-1:
                    d = d
                else:
                    d = 7 - d
            if cs % (2*(C-1)) <= C-1:
                nc = cs % (2*(C-1))
            else:
                nc = 2*(C-1) - cs % ((2*(C-1)))
        # 이동한 상어들 정보 딕셔너리에 저장
        # print(f"방향:{d} {[r, c]} to {[nr, nc]}")
        if (nr, nc) not in shark_pos.keys():
            shark_pos.setdefault((nr, nc), [])
        else:
            M -= 1
        shark_pos[(nr, nc)].append([z, s, d])

    # 딕셔너리에서 상어들을 다시 큐에 넣기
    for k, v in shark_pos.items():
        r, c = k
        z, s, d = max(shark_pos[k])
        sharks[r][c] = z
        que.append((r, c, s, d, z))
    # print(shark_pos)


R, C, M = map(int, input().split())
que = deque()
sharks = [[0]*C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    que.append((r-1, c-1, s, d, z))
    sharks[r-1][c-1] = z
ans = 0
K = -1
while K < C-1:
    if M == 0:
        break
    # print(">>>>>before catch>>>>>", que)
    K += 1
    # print(">>>>>K>>>>>>", K)
    ans += catch(K)
    # print(">>>>>after catch>>>>>", que)
    shark_move(que)
    # print("------------------------------")
# print(">>>>>>ans>>>>>>", ans)
print(ans)