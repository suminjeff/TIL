import sys

sys.stdin = open("최대 상금.txt", "r")

T = int(input())
for tc in range(1, T+1):
    input_num, swap = map(int, input().split())
    input_arr = [int(str(input_num)[x]) for x in range(len(str(input_num)))]
    N = len(input_arr)
    possible_ways = []

    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(j)
        if len(subset) == 2:
            possible_ways.append(subset)

    arr_list = [[swap, input_num]]
    max_v = 0
    i = 0
    while arr_list[0][0] > 0:
        if arr_list:
            swap, input_num = arr_list.pop(0)
            swap -= 1
            arr = list(str(input_num))
            cnt = 0
            for w in possible_ways:
                arr[w[0]], arr[w[1]] = arr[w[1]], arr[w[0]]
                if arr[i] == max(arr[i:]):
                    if max_v < int("".join(arr)):
                        max_v = int("".join(arr))
                        arr_list.append([swap, int("".join(arr))])
                arr[w[0]], arr[w[1]] = arr[w[1]], arr[w[0]]
            i += 1
        if not arr_list:
            break
    print(f"#{tc} {max_v}")
