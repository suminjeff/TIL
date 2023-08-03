import sys
sys.stdin = open("이진 탐색.txt", "r")


def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return 1
        elif a[middle] > key:
            end = middle -1
        else:
            start = middle + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    book = [page for page in range(1, P+1)]

    if binarySearch(book, P, Pa) == binarySearch(book, P, Pb):
        result = 0
    if binarySearch(book, P, Pa) == 1 and binarySearch(book, P, Pb) == 0:
        result = "A"
    if binarySearch(book, P, Pb) == 1 and binarySearch(book, P, Pa) == 0:
        result = "B"

    print(f"#{tc} {result}")
