import sys
sys.stdin = open("백만 장자 프로젝트.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    idx = 0
    total = 0



    print(f"#{tc} {total}")
