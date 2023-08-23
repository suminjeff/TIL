import sys

sys.stdin = open('단순 2진 암호코드.txt', 'r')


decode = {"0001101": 0,
          "0011001": 1,
          "0010011": 2,
          "0111101": 3,
          "0100011": 4,
          "0110001": 5,
          "0101111": 6,
          "0111011": 7,
          "0110111": 8,
          "0001011": 9}


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    start_r = 0
    start_c = 0
    found = False
    while not found:
        for i in range(N):
            for j in range(M-1, -1 ,-1):
                if arr[i][j] == "1":
                    start_r = i
                    start_c = j
                    found = True
                    break

    code = list(arr[start_r][start_c-55:start_c+1])
    code_list = []
    while len(code_list) != 8:
        temp = ""
        if code:
            while len(temp) != 7:
                temp += code.pop(0)
        code_list.append(decode[temp])
    check = 0
    for i in range(4):
        check += code_list[2*i]*3
        check += code_list[2*i+1]
    ans = 0
    if check % 10 == 0:
        ans = sum(code_list)
    print(f"#{tc} {ans}")