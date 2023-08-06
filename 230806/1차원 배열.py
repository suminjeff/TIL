import sys
sys.stdin = open("1차원 배열.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = 0

    for i in range(N):
        count = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                count += 1

        if max_v < count:
            max_v = count

    print(f"#{tc} {max_v}")