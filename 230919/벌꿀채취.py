import sys
sys.stdin = open("벌꿀채취.txt", "r")


def dfs(L, P):
    global MP
    global N
    global M

    if L == M:
        MP = max(MP, P)
        return
    for i in range(N):
        for j in range(N-M+1):
            if not visited[i][j] and j + M < N:
                P = 0
                visited[i][j] = 1
                for k in range(j, j+M):
                    P += hive[i][k]**2
                dfs(M, P)
                visited[i][j] = 0


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    hive = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    MP = 0

    for r in range(N):
        for c in range(N-M+1):
            profit = 0
            honey1 = []
            # 일꾼1이 채취한 꿀 표시
            for m in range(c, c+M):
                visited[r][m] = 1
                honey1.append(hive[r][m])
            if sum(honey1) > C:
                stack1 = []
                honey1.sort()
                while sum(stack1) <= C:
                    stack1.append(honey1.pop())
                for s1 in stack1:
                    profit += s1**2
            else:
                for h1 in honey1:
                    profit += h1 ** 2

            for i in range(N):
                for j in range(N-M+1):
                    if j+M-1 < N:
                        temp = profit
                        honey2 = []
                        flag = True
                        for k in range(j, j+M):
                            if visited[i][k] == 1:
                                flag = False
                        if flag:
                            for k in range(j, j+M):
                                honey2.append(hive[i][k])
                            if sum(honey2) > C:
                                stack2 = []
                                honey2.sort()
                                while sum(stack2) <= C:
                                    stack2.append(honey2.pop())
                                for s2 in stack2:
                                    profit += s2 ** 2
                            else:
                                for h2 in honey2:
                                    profit += h2 ** 2
                            print(honey1, honey2)
                            MP = max(MP, temp)
                    else:
                        continue

            # 일꾼1이 채취한 꿀 초기화
            for m in range(c, c+M):
                visited[r][m] = 0
            print()

    print(f"#{tc} {MP}")