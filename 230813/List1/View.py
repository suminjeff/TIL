import sys

sys.stdin = open("View.txt", "r")

T = 10

for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))
    delta = [-2, -1, 1, 2]

    ans = 0
    for i in range(2, N-2):
        max_v = 0
        view = True
        for k in range(4):
            ni = i + delta[k]
            if arr[ni] >= arr[i]:
                view = False
                break
            if max_v < arr[ni]:
                max_v = arr[ni]
        if view:
            ans += arr[i] - max_v

    print(f"#{tc} {ans}")