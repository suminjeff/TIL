import sys

sys.stdin = open("특별한 정렬.txt", "r")


def bubble_up(num_list, length):
    for i in range(length-1):
        for j in range(length-1 - i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list


def bubble_down(num_list, length):
    for i in range(length-1):
        for j in range(length-1 - i):
            if num_list[j] < num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for i in range(5):
        bubble_down(arr, N)
        ans.append(arr[i])
        bubble_up(arr, N)
        ans.append(arr[i])
    print(f"#{tc}", *ans)
