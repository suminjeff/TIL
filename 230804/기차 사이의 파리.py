import sys
sys.stdin = open("기차 사이의 파리.txt")

T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    for i in range(D):
        F += i



    print(f"#{tc} {rail}")