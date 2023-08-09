import sys
sys.stdin = open("괄호 검사.txt", "r")


def check_brackets(brackets):
    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
        if b == ")":
            if not stack:
                return -1
            else:
                stack.pop()
    if not stack:
        return 1
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    brackets = input()
    print(f"#{tc} {check_brackets(brackets)}")
