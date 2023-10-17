import sys
sys.stdin = open('아기 상어2.txt', 'r')
input = sys.stdin.readline

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 9: 아기상어의 위치
    # 1~6: 물고기의 크기
    # 이동 조건
    # 1. 자신보다 크기가 큰 물고기가 있는 칸은 지날 수 없고 나머지 (같거나 작은) 칸은 모두 지날 수 있음
    # 2. 자신보다 크기가 작은 물고기만 먹을 수 있음
    # 이동 방법
    #     a) 더 이상 먹을 수 있는 물고기가 없다면 어미 상어에게 도움을 청한다. x
    #     b) 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 간다. x
    #     c) 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    #         i. 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 떄, 지나야하는 칸의 개수의 최솟값
    #        ii. 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다
    # 2. 이동은 1초 걸리고, 물고기를 먹는 데에 걸리는 시간은 없다고 가정 (즉, 이동 즉시 먹음)
    #     - 물고기를 먹으면 그 칸은 빈 칸이 됨
    # 3. 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
    # 문제 : 아기 상어가 몇 초 동안 엄마 상어에게 도움을 청하지 않고 물고기를 잡아먹을 수 있는지 구하기

    # 아기 상어의 위치와 먹을 수 있는 물고기의 개수 세기
    baby_shark_size = 2
    baby_shark_pos = []
    fish_N = 0
    for i in range(N):
        for j in range(N):
            if 1 <= arr[i][j] < baby_shark_size:
                fish_N += 1
            elif arr[i][j] == 9:
                baby_shark_pos = [i, j]

    # 물고기가 모두 없어질 동안 반복 (엄마 상어에게 도움을 청하기 직전까지)
    # T = 지난 시간
    eat_cnt = 0
    T = 0
    while fish_N > 0:
        print(">>>>>baby_shark_pos", baby_shark_pos)
        print(">>>>>baby_shark_size", baby_shark_size)
        print(">>>>>eat_cnt", eat_cnt)
        print(">>>>>T", T)
        print(">>>>>fish_N", fish_N)
        print(*arr, sep="\n")
        # 먹을 수 있는 물고기가 1개보다 많을 때
        # 가장 가까운 물고기를 먹으러 간다 (자신보다 큰 물고기가 있는 칸은 지날 수 없음)
        arr[baby_shark_pos[0]][baby_shark_pos[1]] = 0
        que = deque()
        que.append([baby_shark_pos[0], baby_shark_pos[1], T])
        eat_fish = False
        visited = [[0]*N for _ in range(N)]
        visited[baby_shark_pos[0]][baby_shark_pos[1]] = 1
        while que:
            r, c, t = que.popleft()
            for nr, nc in [[r-1, c], [r, c-1], [r, c+1], [r+1, c]]:
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                    if 0 < arr[nr][nc] < baby_shark_size:
                        t += 1
                        visited[nr][nc] = 1
                        eat_cnt += 1
                        if eat_cnt == baby_shark_size:
                            eat_cnt = 0
                            baby_shark_size += 1
                        arr[nr][nc] = 0
                        baby_shark_pos = [nr, nc]
                        eat_fish = True
                        print(f"--------eat moved to {[nr, nc]}---------")
                        break
                    elif baby_shark_size >= arr[nr][nc]:
                        visited[nr][nc] = 1
                        que.append([nr, nc, t+1])
            if eat_fish:
                canContinue = False
                edible_fish = 0
                for i in range(N):
                    for j in range(N):
                        if 0 < arr[i][j] < baby_shark_size:
                            canContinue = True
                            edible_fish += 1
                fish_N = edible_fish
                T = t
                break


    print(f"#{tc} {T}")
    print("---------END----------")
