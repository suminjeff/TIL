import sys

sys.stdin = open("목차 세기.txt", "r")

N = int(input())
arr = [int(input()) for _ in range(N)]
stack = []
i = 0
while i < N:
    if arr[i] == 1:
        stack.append(arr[i])
        i += 1
        while arr[i] != 1:
            stack.append(arr[i])
            i += 1



print(arr)