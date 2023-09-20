import sys
sys.stdin = open("벌꿀채취.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    hive = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    max_profit = 0

    for r in range(N):
        for c in range(N):
            if c+M-1 < N:
                # 일꾼 1 벌꿀 채취
                visited = [[0]*N for _ in range(N)]
                honey1 = []
                for k1 in range(c, c+M):
                    visited[r][k1] = 1
                    honey1.append(hive[r][k1])
                profit1 = 0
                if sum(honey1) > C:
                    subset_list1 = []
                    for i1 in range(1 << len(honey1)):
                        subset1 = []
                        for j1 in range(len(honey1)):
                            if i1 & (1 << j1):
                                subset1.append(honey1[j1])
                        if subset1:
                            if sum(subset1) <= C:
                                temp1 = 0
                                for s1 in subset1:
                                    temp1 += s1 ** 2
                                    profit1 = max(profit1, temp1)
                else:
                    for h1 in honey1:
                        profit1 += h1**2
                # 일꾼 2의 경우의 수
                for row in range(N):
                    for col in range(N):
                        if col+M-1 < N:
                            flag = True
                            for m in range(col, col+M):
                                if visited[row][m]:
                                    flag = False
                                    break
                            if flag:
                                honey2 = []
                                for k2 in range(col, col+M):
                                    honey2.append(hive[row][k2])
                                profit2 = 0
                                if sum(honey2) > C:
                                    subset_list1 = []
                                    for i2 in range(1 << len(honey2)):
                                        subset2 = []
                                        for j2 in range(len(honey2)):
                                            if i2 & (1 << j2):
                                                subset2.append(honey2[j2])
                                        if subset2:
                                            if sum(subset2) <= C:
                                                temp2 = 0
                                                for s2 in subset2:
                                                    temp2 += s2 ** 2
                                                    profit2 = max(profit2, temp2)
                                else:
                                    for h1 in honey2:
                                        profit2 += h1 ** 2
                                profit = profit1 + profit2
                                max_profit = max(max_profit, profit)

    print(f"#{tc} {max_profit}")