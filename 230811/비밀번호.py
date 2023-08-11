import sys

sys.stdin = open("비밀번호.txt", "r")

T = 10
for tc in range(1, T+1):
    N, arr = input().split()
    N = int(N)
    arr = list(arr)
    i = N-1
    while i > 0:
        if arr[i] == arr[i-1]:
            arr.pop(i)
            arr.pop(i-1)
            i = len(arr) - 1
        else:
            i -= 1

    print(f"#{tc} {''.join(arr)}")