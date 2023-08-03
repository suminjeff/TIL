import sys
sys.stdin = open("부분집합의 합.txt", "r")


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
    N, K = map(int, input().split())
    arr = [n+1 for n in range(12)]
    n = len(arr)

    subset_list = []
    count = 0

    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        subset_list.append(subset)
    for subsets in subset_list:
        if my_len(subsets) == N and my_sum(subsets) == K:
            count += 1
    print(f"#{tc} {count}")
