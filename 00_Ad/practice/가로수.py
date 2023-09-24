import sys
sys.stdin = open("가로수.txt", "r")
input = sys.stdin.readline

N = int(input())
trees = [int(input()) for _ in range(N)]
diff = set()
for i in range(1, N):
    diff.add(abs(trees[i]-trees[i-1]))
print(diff)
cnt = 0
for j in range(min(trees), max(trees)+1, min(diff)):
    if j not in trees:
        cnt += 1
print(cnt)