def binary_search(arr, n, key):
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == key:
            return True
        elif arr[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False
