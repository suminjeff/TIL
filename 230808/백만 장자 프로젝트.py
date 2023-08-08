import sys

sys.stdin = open("백만 장자 프로젝트.txt", "r")


def my_max(starting, n_list):
    max_v = n_list[starting]
    for n in range(starting, my_len(n_list)):
        if max_v < n_list[n]:
            max_v = n_list[n]
    return max_v


def my_len(n_list):
    length = 0
    for _ in n_list:
        length += 1
    return length


def my_idx(n_list, starting, key):
    for idx in range(starting, my_len(n_list)):
        if n_list[idx] == key:
            return idx


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    total_profit = 0
    start = 0

    while start < N:
        # temp = arr[start:]
        end = my_idx(arr, start, my_max(start, arr))
        for i in range(start, end):
            profit = arr[end] - arr[i]
            total_profit += profit
        start = end + 1
        #################

    print(f"#{tc} {total_profit}")
