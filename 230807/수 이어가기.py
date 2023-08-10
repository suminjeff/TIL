import sys

sys.stdin = open("수 이어가기.txt", "r")

N = int(input())
max_count = 0

for i in range(1, N + 1):
    my_list = []
    num = N - i
    while num >= 0:

    if max_count < len(my_list):
        max_count = len(my_list)

print(max_count)