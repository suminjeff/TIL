import sys
sys.stdin = open('원자 소멸 시뮬레이션.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {atoms}")
