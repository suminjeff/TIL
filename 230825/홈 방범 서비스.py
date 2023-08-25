import sys

sys.stdin = open('홈 방범 서비스.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    max_list = []
    for i in range(N):
        for j in range(N):
            # 방문표시 배열 생성 후 방문 표시
            visited = [[0]*(N+1) for _ in range(N+1)]
            visited[i][j] = 1

            # 초기 K = 1, 그에 따라 매출은 M, 비용은 1, 수익은 M-1
            K = 1
            cnt = int(arr[i][j])
            sales = M * cnt
            cost = K**2 + (K-1)**2

            revenue = sales - cost
            temp_que = [[i, j]]
            while K < N+2:
                K += 1
                sales = M * cnt
                cost = K ** 2 + (K - 1) ** 2
                revenue = sales - cost
                que = []
                while temp_que:
                    r, c = temp_que.pop(0)
                    for k in range(4):
                        nr, nc = r + dr[k], c + dc[k]
                        if 0 <= nr < N and 0 <= nc < N and [nr, nc] not in que:
                            if not visited[nr][nc]:
                                que.append([nr, nc])
                temp_que = que[:]
                while que:
                    p, q = que.pop(0)
                    if arr[p][q] == 1 and not visited[p][q]:
                        visited[p][q] = 1
                        cnt += 1
                    else:
                        visited[p][q] = 1
                        continue
                    sales = M * cnt
                    cost = K ** 2 + (K - 1) ** 2
                    revenue = sales - cost
                    if revenue >= 0:
                        max_list.append(cnt)

    print(f"#{tc} {max(max_list)}")