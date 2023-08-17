import sys

sys.stdin = open("이진 탐색.txt", "r")


T = int(input())
for tc in range(1, T+1):
    book = [0] * 1001
    P, A, B = map(int, input().split())
    C = int((1 + P)/2)
    cnt_A = 0
    cnt_B = 0
    L_A = 1
    R_A = P
    while C != A:
        C = int((L_A+R_A)/2)
        if C == A:
            cnt_A += 1
            break
        elif C < A:
            L_A = C+1
            cnt_A += 1
        elif C > A:
            R_A = C-1
            cnt_A += 1
    L_B = 1
    R_B = P
    while C != B:
        C = int((L_B+R_B)/2)
        if C == B:
            cnt_B += 1
            break
        elif C < B:
            L_B = C+1
            cnt_B += 1
        elif C > B:
            R_B = C-1
            cnt_B += 1
    if cnt_A < cnt_B:
        print(f"#{tc} A")
    elif cnt_A == cnt_B:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} B")
