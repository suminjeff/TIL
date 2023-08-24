import sys

sys.stdin = open('암호비트패턴 출력하기.txt', 'r')


BP = {
    "001101": 0,
    "010011": 1,
    "111011": 2,
    "110001": 3,
    "100011": 4,
    "110111": 5,
    "001011": 6,
    "111101": 7,
    "011001": 8,
    "101111": 9,
}

T = int(input().strip())
for tc in range(1, T+1):
    hex_code = input().strip()
    N = len(hex_code) * 4
    bin_code = ""
    for i in hex_code:
        bc = bin(int(i, 16)).lstrip("0b").zfill(4)
        bin_code += bc

    ans = []
    start = N-1
    while start >= 0:
        if bin_code[start] == "1":
            code = ""
            for j in range(6):
                code += bin_code[start-j]
            code = list(code)
            code.reverse()
            code = "".join(code)
            ans.append(BP[code])
            start -= 6

        else:
            start -= 1
    ans.reverse()
    print(f"#{tc}", *ans)