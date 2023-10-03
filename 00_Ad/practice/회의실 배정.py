import sys
sys.stdin = open("회의실 배정.txt", "r")
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))
stack = []
cnt = 0
for start, end in meetings:
    if stack:
        if start >= stack[-1]:
            stack.append(start)
            stack.append(end)
            cnt += 1
    else:
        stack.append(start)
        stack.append(end)
        cnt += 1
print(cnt)