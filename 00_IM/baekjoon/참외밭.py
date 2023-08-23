import sys

sys.stdin = open('참외밭.txt', 'r')

# K = 1제곱미터에 자라는 참외 개수
K = int(input())

max_width = 0
max_width_idx = 0
max_height = 0
max_height_idx = 0
arr = []
for i in range(6):
    direction, meter = map(int, input().split())
    arr.append([direction, meter])
    if direction == 1 or direction == 2:
        if max_width < meter:
            max_width = meter
            max_width_idx = i
    elif direction == 3 or direction == 4:
        if max_height < meter:
            max_height = meter
            max_height_idx = i

min_width = 0
min_height = 0
if (max_height_idx + 1) % 6 < (max_width_idx + 1) % 6 or ((max_width_idx + 1) % 6 == 0 and (max_height_idx + 1) % 6 == 5):
    min_width_idx = (max_width_idx+2) % 6
    min_height_idx = (max_height_idx+4) % 6
    min_width = arr[min_width_idx][1]
    min_height = arr[min_height_idx][1]
elif (max_width_idx + 1) % 6 < (max_height_idx + 1) % 6 or ((max_height_idx + 1) % 6 == 0 and (max_width_idx + 1) % 6 == 5):
    min_width_idx = (max_width_idx+4) % 6
    min_height_idx = (max_height_idx+2) % 6
    min_width = arr[min_width_idx][1]
    min_height = arr[min_height_idx][1]

ans = K * (max_width * max_height - min_width * min_height)
print(ans)