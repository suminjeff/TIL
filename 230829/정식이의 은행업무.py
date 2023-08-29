import sys

sys.stdin = open('정식이의 은행업무.txt', 'r')


def compare(original, comparing):
    n = len(original)
    cnt = 0
    for x in range(n):
        if original[x] != comparing[x]:
            cnt += 1
    return cnt


def ternary_to_dec(ternary):
    ternary.reverse()
    n = len(ternary)
    res = 0
    for x in range(n):
        res += int(ternary[x]) * (3 ** x)
    ternary.reverse()
    return res


def binary_to_dec(binary):
    binary.reverse()
    n = len(binary)
    res = 0
    for x in range(n):
        res += int(binary[x]) * (2 ** x)
    binary.reverse()
    return res


def dec_to_ternary(dec):
    ternary_num = ""
    while dec:
        ternary_num += str(dec % 3)
        dec //= 3
    ternary_num = ternary_num.zfill(len(tricode_original))
    ternary_num = list(ternary_num)
    ternary_num.reverse()
    return ternary_num


T = int(input())
for tc in range(1, T+1):
    bicode_original = list(input())
    tricode_original = list(input())
    N = len(bicode_original)
    for i in range(N):
        bicode = bicode_original[:]
        bicode[i] = str(1 - int(bicode_original[i]))
        dec = binary_to_dec(bicode)
        tricode = dec_to_ternary(dec)
        if compare(tricode_original, tricode) == 1:
            print(f"#{tc} {dec}")
            break
