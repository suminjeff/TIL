import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

    print(f"#{tc}")