import sys
sys.stdin = open("좌표 정렬하기.txt", "r")
input = sys.stdin.readline

N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]
coords.sort()
for x, y in coords:
    print(x, y)