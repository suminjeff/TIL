import sys

sys.stdin = open("패턴 마디의 길이.txt", "r")

T = int(input())
for tc in range(1, T+1):
    input_str = input()
    pattern = ""
    checker = ""
    ans = 0
    for i in range(len(input_str)):
        if pattern:
            if input_str[i] == pattern[0]:
                for j in range(i, i+i):
                    checker += input_str[j]
                if pattern == checker:
                    ans += len(pattern)
                    break
                else:
                    pattern += input_str[i]
                    checker = ""
            else:
                pattern += input_str[i]
        else:
            pattern += input_str[i]

    print(f"#{tc} {ans}")