import sys
sys.stdin = open("비밀번호.txt", "r")

T = 10
for tc in range(1, T+1):
    N, pwd = input().split()
    idx = int(N)-1
    pwd = list(pwd)
    while idx > 0:
        if pwd[idx] == pwd[idx-1]:
            pwd.pop(idx)
            pwd.pop(idx-1)
            idx = len(pwd) - 1
        else:
            idx -= 1
    print(f"#{tc}", end=" ")
    print(*pwd, sep="")