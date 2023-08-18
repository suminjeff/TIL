import sys

sys.stdin = open("미로의 거리.txt", "r")

# 1.

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # 시작점 찾기
    pos = []
    for i in range(N):
        if '2' in arr[i]:
            pos.append(i)
            pos.append(arr[i].index('2'))

    # 델타 탐색 좌표 설정
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # BFS를 위한 큐
    queue = [pos]
    # 방문표시 배열과 초기 설정
    vstd = [[0] * N for _ in range(N)]
    vstd[pos[0]][pos[1]] = 1
    # 정답 초기 설정(BFS로 3이 안찾아지면 그대로 0)
    ans = 0
    while queue:
        # 현재 위치의 행, 열값
        r, c = queue.pop(0)
        # 델타 탐색
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 미로 범위 내에 있는지 + 방문안했던 노드인지
            if 0 <= nr < N and 0 <= nc < N and vstd[nr][nc] == 0:
                # 갈 수 있는 길이라면 vstd에 현재 위치의 +1씩 표시
                if arr[nr][nc] == '0':
                    vstd[nr][nc] = vstd[r][c] + 1
                    # 큐에 대기시키기
                    queue.append([nr, nc])
                    # 3을 찾았다면 시작&끝점의 개수를 뺀 값이 정답
                elif arr[nr][nc] == '3':
                    vstd[nr][nc] = vstd[r][c] + 1
                    ans = vstd[nr][nc] - 2

    print(f"#{tc} {ans}")
