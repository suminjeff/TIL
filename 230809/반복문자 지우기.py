import sys

sys.stdin = open("반복문자 지우기.txt", "r")


def my_len(iterable):
    length = 0
    for _ in iterable:
        length += 1
    return length


T = int(input())
for tc in range(1, T+1):
    string = list(input())
    top = my_len(string) - 1
    while top >= 1:
        if string[top] == string[top - 1]:
            string.pop(top)
            string.pop(top - 1)
            top = my_len(string) - 1
        else:
            top -= 1
    print(f"#{tc} {my_len(string)}")