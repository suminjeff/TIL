import sys
sys.stdin = open("알고리즘 수업 - 병합 정렬 1.txt", "r")
input = sys.stdin.readline


def merge_sort(arr):
    global cnt
    global ans
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
        cnt += 1

    merged += left[l:]
    merged += right[r:]
    return merged


N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
ans = 0
merge_sort(arr)
# merged = merge_sort(arr)
print(cnt)