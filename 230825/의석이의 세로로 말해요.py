import sys

sys.stdin = open('의석이의 세로로 말해요.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    max_len = 0
    for string in arr:
        str_length = len(string)
        if max_len < str_length:
            max_len = str_length

    print(f"#{tc} ", end="")
    for i in range(max_len):
        for j in range(5):
            if i < len(arr[j]):
                print(arr[j][i], end="")
    print()