import sys

sys.stdin = open('16진수를 10진수로 변환하기.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    hex_code = input()
    bin_code = ""
    for i in hex_code:
        bc = bin(int(i, 16)).lstrip("0b").zfill(4)
        bin_code += bc
    bin_code = list(bin_code)

    bin_split = []
    flag = True
    while flag:
        temp = ""
        for j in range(7):
            if bin_code:
                temp += (bin_code.pop(0))
            else:
                flag = False
                break
        bin_split.append(int(temp, 2))
    print(f"#{tc}", *bin_split)
