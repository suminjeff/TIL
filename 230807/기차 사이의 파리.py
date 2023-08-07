import sys
sys.stdin = open("기차 사이의 파리.txt", "r")

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    time = D/(A+B)
    fly = time * F
    print(f"#{tc} {fly}")