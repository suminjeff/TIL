import sys

sys.stdin = open("괄호 검사.txt", "r")


def bracket_check(brackets):
    stack = []
    for i in brackets:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return -1
            else:
                stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    brackets = input()
    print(f"#{tc} {bracket_check(brackets)}")