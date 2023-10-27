import sys
sys.stdin = open('스택 수열.txt', 'r')
input = sys.stdin.readline

N = int(input())
input_arr = [int(input()) for _ in range(N)]
arr = [i for i in range(N, 0, -1)]
stack = []
idx = 0
ans = []
while arr:
    stack.append(arr.pop())
    ans.append('+')
    if stack[-1] == input_arr[idx]:
        while stack:
            if stack[-1] == input_arr[idx]:
                stack.pop()
                ans.append('-')
                idx += 1
            else:
                break
if stack:
    print("NO")
else:
    print(*ans, sep="\n")