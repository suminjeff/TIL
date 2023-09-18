import sys
sys.stdin = open("병합 정렬.txt", "r")


def merge(arr):
    global cnt

    n = len(arr)
    if n == 1:
        return

    middle = n//2
    left, right = arr[0:middle], arr[middle:n]

    if max(left) > max(right):
        cnt += 1
    merge(left)
    merge(right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merge(arr)
    arr.sort()

    print(f"#{tc} {arr[N//2]} {cnt}")