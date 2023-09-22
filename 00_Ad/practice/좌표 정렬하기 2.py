import sys

sys.stdin = open("좌표 정렬하기 2.txt", "r")
input = sys.stdin.readline

N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]
coords.sort(key=lambda x: (x[1], x[0]))
for x, y in coords:
    print(x, y)
