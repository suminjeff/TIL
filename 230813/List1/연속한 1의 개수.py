import sys

sys.stdin = open("연속한 1의 개수.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    string = input()

    ans = 0
    temp = 0
    for i in range(N):
        if string[i] == '1':
            temp += 1
        else:
            temp = 0
        if ans < temp:
            ans = temp

    print(f"#{tc} {ans}")