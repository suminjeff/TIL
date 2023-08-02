import sys
sys.stdin = open("input.txt", "r")


def my_sum(num_list):
    result = 0
    for num in num_list:
        result += num
    return result


def my_max(num_list):
    max_num = num_list[0]
    for num in num_list:
        if max_num < num:
            max_num = num
    return max_num


# T = int(input())
T = 10
for tc in range(1, T+1):
    N = int(input())
    # 2차원 배열 입력받기 (range = 세로 길이)
    arr = [list(map(int, input().split())) for _ in range(100)]
    temp = []
    for i in range(100):
        temp.append(my_sum(arr[i]))  # 행의 합
        col = 0
        for j in range(100):
            col += arr[j][i]         # 열의 합
        temp.append(col)
        temp.append(arr[i][i])       # 우하향 대각의 합
        temp.append(arr[i][99-i])    # 좌하향 대각의 합

    print(f"#{N} {my_max(temp)}")

    # for i in range(100):
    #     if max_v < my_sum(arr[i]):
    #         max_v = my_sum(arr[i])
    #
    # for i in range(100):
    #     col = 0
    #     for j in range(100):
    #         col += arr[j][i]
    #     if max_v < col:
    #         max_v = col
    #
    # for i in range(100):
    #     total = 0
    #     total += arr[i][i]
    #     if max_v < total:
    #         max_v = total
    #
    # for i in range(100):
    #     total = 0
    #     total += arr[i][99-i]
    #     if max_v < total:
    #         max_v = total
    #
    # print(f"#{N} {max_v}")