import sys

sys.stdin = open("이진 탐색.txt", "r")


def b_search(array, end, key):
    left = 0
    right = end - 1
    count = 0
    while left <= right:
        center = int((left + right) / 2)
        if array[center] == key:
            count += 1
            return count
        elif array[center] > key:
            right = center - 1
            count += 1
        else:
            left = center + 1
            count += 1
    return count


T = int(input())
for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    book = [page for page in range(1, P + 1)]

    a = b_search(book, P, Pa)
    b = b_search(book, P, Pb)

    result = 0

    if a < b:
        result = "A"
    elif a > b:
        result = "B"

    print(f"#{tc} {result}")
