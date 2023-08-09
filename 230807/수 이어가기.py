import sys

sys.stdin = open("수 이어가기.txt", "r")

N = int(input())
max_count = 0

for i in range(1, N + 1):
    num = N - i
    count = 0
    my_list = []
    while num >= 0:
        num = i - num
        count += 1
        if max_count < count:
            max_count = count

print(max_count)