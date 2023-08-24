import sys

sys.stdin = open('암호코드 스캔.txt', 'r')


BP_ratio = {
    [3, 2, 1, 1]: 0,
    [2, 2, 2, 1]: 1,
    [2, 1, 2, 2]: 2,
    [1, 4, 1, 1]: 3,
    [1, 1, 3, 2]: 4,
    [1, 2, 3, 1]: 5,
    [1, 1, 1, 4]: 6,
    [1, 3, 1, 2]: 7,
    [1, 2, 1, 3]: 8,
    [3, 1, 1, 2]: 9,
}



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 16진수 한자리를 2진수 네자리수로 만들기
    for i in range(N):
        for j in range(M):
            hex_v = arr[i][j]
            bin_v = bin(int(hex_v, 16)).lstrip("0b").zfill(4)
            arr[i][j] = bin_v

    # 2진수 합치기
    bin_code = []
    for r in range(N):
        temp = "".join(arr[r]).rstrip("0")
        if temp:
            bin_code.append(temp)

    # 암호 찾기
    code_list = set()
    for i2 in range(len(bin_code)):
        ans = []
        start = len(bin_code[i2]) - 1
        while start >= 0:
            ratio = []
            while True:
                if bin_code[i2][start] == "1":
                    cnt = 0
                    while bin_code[i2][start] == "1":
                        cnt += 1
                        start -= 1
                    ratio.append(cnt)
                elif bin_code[i2][start] == "0":
                    cnt = 0
                    while bin_code[i2][start] == "0":
                        cnt += 1
                        start -= 1
                    ratio.append(cnt)
            ratio.reverse()



            # else:
            #     start -= 1

    print(f"#{tc} {bin_code}")