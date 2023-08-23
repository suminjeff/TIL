import sys

sys.stdin = open('참외밭.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print(f"#{tc}")

# K = 1제곱미터에 자라는 참외 개수
K = int(input())

drc = []
zig = []
wh = [[] for _ in range(5)]
new = []
front = 0
rear = 0
for _ in range(6):
    d, m = map(int, input().split())
    wh[d].append(m)
    if d in drc:
        zig.append(d)
    drc.append(d)
    new.append([d, m])

for i in range(6):
    if new[i][0] == 4:
        for i in range(i):
            popped = new.pop(0)
            new.append(popped)
max_h = 0
max_w = 0
for i in range(6):
    if new[i][0] == 1 or new[i][0] == 2:
        if max_w < new[i][1]:
            max_w = new[i][1]
    if new[i][0] == 3 or new[i][0] == 4:
        if max_h < new[i][1]:
            max_h = new[i][1]

max_area = max_h * max_w
if new[0][1] == max_h:
else:

print(ans)