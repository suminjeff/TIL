import sys

sys.stdin = open("이진 탐색.txt", "r")


def binary_search(t, n):
    left = 0
    right = n-1
    flag = "start"
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == t:
            return True
        elif t < arr[mid] and flag != "left":
            right = mid-1
            flag = "left"
        elif t > arr[mid] and flag != "right":
            left = mid+1
            flag = "right"
        else:
            return False


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    targets = list(map(int, input().split()))
    cnt = 0
    for target in targets:
        if binary_search(target, N):
            cnt += 1

    print(f"#{tc} {cnt}")