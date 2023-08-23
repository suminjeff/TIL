import sys

sys.stdin = open('이진수.txt', 'r')

hex_dict = {'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15}


T = int(input())
for tc in range(1, T+1):
    N, hex_n = input().split()
    bin_n = ""
    for i in range(int(N)):
        if hex_n[i].isnumeric():
            bin_n += bin(int(hex_n[i])).lstrip("0b").zfill(4)
        else:
            bin_n += bin(hex_dict[hex_n[i]]).lstrip("0b").zfill(4)
    print(f"#{tc} {bin_n}")
