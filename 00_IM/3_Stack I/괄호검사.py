T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = []
    for i in string:
        if i == "(":
            stack.append(i)
        