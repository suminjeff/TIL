import sys
sys.stdin = open("합분해.txt", "r")
input = sys.stdin.readline


def backtrack(depth, res):
    global cnt
    if depth > K or res > N:
        return
    if res == N:
        cnt += 1
        return
    for i in range(N):
        backtrack(depth+1, res+arr[i])


N, K = map(int, input().split())
arr = [i for i in range(N)]

# dp =

cnt = 0
backtrack(0, 0)
print(cnt)
# print(cnt % 1000000000)