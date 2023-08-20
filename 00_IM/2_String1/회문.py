import sys

sys.stdin = open("회문.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    flag = True
    ans = 0
    for i in range(N):
        for j in range(N-M+1):
            temp = ""
            for k in range(j, j+M):
                temp += arr[i][k]
            if temp == temp[::-1]:
                ans = temp
    for i in range(N):
        for j in range(N-M+1):
            temp = ""
            for k in range(j, j+M):
                temp += arr[k][i]
            if temp == temp[::-1]:
                ans = temp
    print(f"#{tc} {ans}")