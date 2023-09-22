import sys
sys.stdin = open("가로수.txt", "r")
input = sys.stdin.readline

N = int(input())
trees = [int(input()) for _ in range(N)]
diff = set()
for i in range(1, N):
    diff.add(trees[i]-trees[i-1])
print((trees[-1] - trees[0])//min(diff) - len(trees))