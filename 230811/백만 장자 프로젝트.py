import sys
sys.stdin = open("백만 장자 프로젝트.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.reverse()

    profit = 0
    max_v = arr[0]

    for i in range(N):
        if max_v < arr[i]:
            max_v = arr[i]
        else:
            profit += max_v - arr[i]

    print(f"#{tc} {profit}")
