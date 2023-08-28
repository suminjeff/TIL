import sys

sys.stdin = open("16811.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    limit = N//2
    arr = sorted(list(map(int, input().split())))
    ans = 1000
    for i in range(N-2):
        for j in range(i+1, N-1):
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]:
                small = i+1
                mid = j-i
                large = N-1 - j
                if small <= limit and mid <= limit and large <= limit:
                    temp = max(small, mid, large) - min(small, mid, large)
                    ans = min(ans, temp)
    if ans == 1000:
        ans = -1

    print(f'#{tc} {ans}')
