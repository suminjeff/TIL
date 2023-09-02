import sys

sys.stdin = open("최대 상금.txt", "r")

T = int(input())
for tc in range(1, T+1):
    input_num, swap = map(int, input().split())
    input_arr = [str(input_num)[x] for x in range(len(str(input_num)))]
    N = len(input_arr)
    possible_ways = []

    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(j)
        if len(subset) == 2:
            possible_ways.append(subset)

    res = [[] for _ in range(swap+1)]
    res[0].append(str(input_num))
    for i in range(1, swap+1):
        for arr in res[i-1]:
            arr = list(arr)
            for j in range(len(possible_ways)):
                if arr[possible_ways[j][0]] == arr[possible_ways[j][1]]:
                    continue
                arr[possible_ways[j][0]], arr[possible_ways[j][1]] = arr[possible_ways[j][1]], arr[possible_ways[j][0]]
                swapped_num = "".join(arr)
                if swapped_num not in res[i]:
                    res[i].append(swapped_num)
                arr[possible_ways[j][0]], arr[possible_ways[j][1]] = arr[possible_ways[j][1]], arr[possible_ways[j][0]]
    print(f"#{tc} {max(res[-1])}")