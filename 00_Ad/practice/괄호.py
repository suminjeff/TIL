import sys
sys.stdin = open("괄호.txt", "r")
input = sys.stdin.readline


def brcheck(arr):
    for br in arr:
        if stack:
            if br == "(":
                stack.append(br)
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return "NO"
        else:
            if br == "(":
                stack.append(br)
            else:
                return "NO"
    if stack:
        return "NO"
    else:
        return "YES"


T = int(input())
for tc in range(1, T+1):
    arr = input().rstrip()
    stack = []
    print(brcheck(arr))
