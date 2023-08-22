import sys

sys.stdin = open("사칙연산.txt", "r")


def postorder(n):
    if n:
        postorder(c1[n])
        postorder(c2[n])
        postfix.append(tree[n])


op = {"+": 1,
      "-": 1,
      "*": 2,
      "/": 2}

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    c1 = [0] * (N+1)
    c2 = [0] * (N+1)

    for i in range(1, N+1):
        node = list(input().split())
        if node[1].isnumeric():
            tree[i] = int(node[1])
        else:
            tree[i] = node[1]
            c1[i] = int(node[2])
            c2[i] = int(node[3])
    postfix = []
    stack = []
    postorder(1)
    # for tkn in postfix:
    #     if tkn in op:
    #         if len(postfix) > 1:
    #             b = stack.pop()
    #             a = stack.pop()
    #             if tkn == "+":
    #                 stack.append(a+b)
    #             elif tkn == "-":
    #                 stack.append(a-b)
    #             elif tkn == "*":
    #                 stack.append(a*b)
    #             elif tkn == "/":
    #                 stack.append(a//b)
    #     else:
    #         stack.append(tkn)
    print(f"#{tc} {postfix}")
    # print(f"#{tc} {c1}")
    # print(f"#{tc} {c2}")
