import sys
sys.stdin = open("problem2.txt", "r")
input = sys.stdin.readline

N, M, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
turned = [[0]*M for _ in range(N)]
stack = []
for i in range(N):
    for j in range(N):
        stack.append(arr[i][j])

for j in range(M-1, -1, -1):
    for i in range(N):
        turned[i][j] = stack.pop(0)
for i in range(N):
    print(*turned[i])