import sys

sys.stdin = open("달팽이 정렬.txt", "r")


def selection_sort(arr, n):
    for i in range(n-1):
        min_i = i
        for j in range(i+1, n):
            if arr[min_i] > arr[j]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    my_arr = []
    for n in range(N):
        my_arr += list(map(int, input().split()))

    # selection_sort(my_arr, N)


    # 델타 탐색 (우 하 좌 상)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    v = 1
    r = 0
    c = 0


    print(f"#{tc} {my_arr}")