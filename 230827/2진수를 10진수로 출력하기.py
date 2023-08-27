import sys

sys.stdin = open("2진수를 10진수로 출력하기.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input().strip())
    binary = list("".join([input().strip() for _ in range(N)]))
    ans = []
    for i in range(0, len(binary), 7):
        ans.append(int("0b" + "".join(binary[i:i+7]), 2))

    print(f"#{tc}", *ans)