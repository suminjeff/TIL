import sys
sys.stdin = open("쇠막대기 자르기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = input()

    stack = []
    for i in range(len(arr)-1, 0, -1):
        if arr[i] == ")" and arr[i-1] == "(":


    print(f"#{tc} {ans}")