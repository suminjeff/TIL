# import sys
# sys.stdin = open("버블 정렬.txt", "r")

def bubble(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def counting(arr):
    counts = [0] * (max(arr) + 1)
    for i in range(len(arr)):
        counts[arr[i]] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    s_arr = arr[:]
    for i in range(len(s_arr)-1, -1, -1):
        counts[arr[i]] -= 1
        s_arr[counts[arr[i]]] = arr[i]

    return s_arr


def subset(arr):
    n = len(arr)
    subset_list = []
    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(arr[j])
        subset_list.append(subset)
    return subset_list


def binarySearch(arr, key):
    N = len(arr)
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return False


def selection(arr):
    N = len(arr)
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr



arr = [231, 23, 6, 123, 345, 12]
print(selection(arr))