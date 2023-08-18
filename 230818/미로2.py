import sys

sys.stdin = open("미로2.txt", "r")

N = 100
T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(input()) for _ in range(N)]

    # 가지치기를 위한 델타값 설정
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    i = 0

    # 시작점 찾기 (tc는 다 (1, 1)이던데 혹시 모르니)
    pos = []
    for row in range(N):
        if '2' in arr[row]:
            pos.append(row)
            pos.append(arr[row].index('2'))

    # 큐 사용
    Q = [pos]

    # 정답 확인용
    flag = False

    # 큐가 비지 않는 동안
    while Q:
        # 현재 좌표
        cur = Q.pop(0)
        # 델타 탐색
        for k in range(4):
            check = [cur[0]+dr[k], cur[1]+dc[k]]
            # 해당 좌표가 미로 범위 내에 있고,
            if 0 <= check[0] < N and 0 <= check[1] < N:
                # 길이 있다면,
                if arr[check[0]][check[1]] == '0':
                    # 큐에 해당 좌표를 넣음
                    Q.append(check)
                    # 해당 좌표값은 '1'로 초기화
                    arr[check[0]][check[1]] = '1'
                # 끝이 있다면,
                elif arr[check[0]][check[1]] == '3':
                    # 답은 True
                    flag = True
                    # 종료조건 발동
                    Q.clear()
                    break
                # 그 외의 상황(끝으로 가는 길이 없다면)들은 BFS 탐색을 모두 하고 큐가 결국 비게 될 것
                # 그래서 따로 종료조건 안만들어줬음

    print(f"#{tc} {int(flag)}")