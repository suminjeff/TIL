import sys

sys.stdin = open("정곤이의 단조 증가하는 수.txt", "r")

for tc in range(1, T+1):
    N = int(input())
    for _ in range(N):
        A = int(input())