import sys
sys.stdin = open("퀵 정렬.txt", "r")


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, middle, right = [], [], []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            middle.append(num)
    return quick_sort(left) + middle + quick_sort(right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = quick_sort(arr)[N//2]
    print(f"#{tc} {ans}")