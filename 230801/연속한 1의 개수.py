import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    string = input()

    cnt = 0
    max_cnt = 0

    for s in string:
        if s == '1':
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 0

    print(f"#{tc} {max_cnt}")