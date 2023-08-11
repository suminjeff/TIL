import sys

sys.stdin = open("1234.txt", "r")

T = 10
for tc in range(1, T+1):
    N, arr = input().split()
    N = int(N)
    arr = list(arr)
    i = len(arr) - 1
    while i > 0:
        if arr[i] == arr[i-1]:
            arr.pop(i)
            arr.pop(i-1)
            i = len(arr)

    print(f"#{tc} {arr}")