import sys
sys.stdin = open("부분집합 합 문제 구현하기.txt", "r")


def my_len(n_list):
    result = 0
    for n in n_list:
        result += 1
    return result


def my_sum(n_list):
    result = 0
    for n in n_list:
        result += n
    return result


T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    n = len(arr)

    subset_list = []
    result = False

    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        subset_list.append(subset)

    for subsets in subset_list:
        if my_len(subsets) > 0 and my_sum(subsets) == 0:
            result = True
    print(f"#{tc} {int(result)}")
