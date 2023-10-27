import sys
sys.stdin = open('덩치.txt', 'r')
input = sys.stdin.readline

N = int(input())
physical = [list(map(int, input().split())) for _ in range(N)]
weight = [0]*201
height = [0]*201
for p in physical:
    weight[p[0]] += 1
    height[p[1]] += 1
print(physical)
