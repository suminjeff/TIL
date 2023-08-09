import sys
sys.stdin = open("비밀번호.txt", "r")


def my_len(iterable):
    length = 0
    for _ in iterable:
        length += 1
    return length


T = 10
for tc in range(1, T+1):
    N, PW = input().split()
    PW = list(PW)
    N = int(N)
    end = N-1

    while end > 0:
        if PW[end] == PW[end-1]:
            PW.pop(end)
            PW.pop(end-1)
            end = my_len(PW) - 1
        else:
            end -= 1

    print(f"#{tc}", end=" ")
    print(*PW, sep="")
