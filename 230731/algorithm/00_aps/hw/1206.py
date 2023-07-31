import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    arr = [0, 0] + list(map(int, input().split())) + [0, 0]
    ans = 0
    for i in range(2, N + 2):
        mini_arr = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
        view = True
        max_v = mini_arr[0]
        for j in range(4):
            if arr[i] < mini_arr[j]:
                view = False
            if max_v < mini_arr[j]:
                max_v = mini_arr[j]
        if view:
            ans += (arr[i] - max_v)
    print(f"#{tc} {ans}")
