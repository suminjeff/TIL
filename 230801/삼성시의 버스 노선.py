import sys

sys.stdin = open("삼성시의 버스 노선.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        A, B = map(int, input().split())
    P = int(input())
    for j in range(P):
        C = int(input())