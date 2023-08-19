import sys
sys.stdin = open("개미.txt", "r")

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
grid = [[0]*(w+1) for _ in range(h+1)]

print(grid)