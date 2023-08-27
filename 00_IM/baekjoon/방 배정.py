import sys

sys.stdin = open("방 배정.txt", "r")

room = [[[0], [0]] for _ in range(6)]

N, K = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]

for gender, grade in students:
    if room[grade-1][gender][-1] < K:
        room[grade-1][gender][-1] += 1
    else:
        room[grade-1][gender].append(1)

cnt = 0
for gr in range(6):
    for gen in range(2):
        if room[gr][gen][0] != 0:
            cnt += len(room[gr][gen])

print(cnt)