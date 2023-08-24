import sys

sys.stdin = open('암호코드 스캔.txt', 'r')

# 뒤집었을 때 거꾸로 비율 : [10진수 값, 첫번째 0들 비율]
BP_ratio = {
    (1, 1, 2): [0, 3],
    (1, 2, 2): [1, 2],
    (2, 2, 1): [2, 2],
    (1, 1, 4): [3, 1],
    (2, 3, 1): [4, 1],
    (1, 3, 2): [5, 1],
    (4, 1, 1): [6, 1],
    (2, 1, 3): [7, 1],
    (3, 1, 2): [8, 1],
    (2, 1, 1): [9, 3],
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
    temp_list = set()
    for r in range(N):
        temp = "".join(arr[r]).strip("0")
        if temp:
            temp.lstrip("0")
            # print(f"#{tc}", temp)
            temp_list.add(temp)
    temp_list = list(temp_list)

    # 이진수 코드를 거꾸로 보면서 비율에 맞게 확인
    need_check = []
    done = []
    for code_block in temp_list:
        end_idx = len(code_block) - 1
        code_block_to_dec = []
        while end_idx >= 0:
            ratio_check = []
            onezero = '1'
            if code_block[end_idx] == "1":
                for _ in range(3):
                    cnt = 0
                    if code_block[end_idx] == onezero:
                        while code_block[end_idx] == onezero:
                            cnt += 1
                            end_idx -= 1
                        onezero = str(1 - int(onezero))
                        ratio_check.append(cnt)
                if 1 in ratio_check:
                    ratio_check = tuple(ratio_check)
                else:
                    divide = 2
                    while True:
                        for i in range(3):
                            ratio_check[i] //= divide
                        if 1 in ratio_check:
                            ratio_check = tuple(ratio_check)
                            break
                if ratio_check in BP_ratio:
                    code_block_to_dec.append(BP_ratio[ratio_check][0])
                # else:
                #     break
            else:
                end_idx -= 1
        if len(code_block_to_dec) > 8:
            need_check.append(code_block_to_dec)
        else:
            done.append(code_block_to_dec)

    # 확인이 필요한 코드라면
    if need_check:
        temp_check_set = set()
        for n in need_check:
            for chop in range(0, len(n)-1, 8):
                temp_check = []
                for i in range(chop, chop+8):
                    temp_check.append(n[i])
                if temp_check not in done:
                    done.append(temp_check)

    # 해독 암호 검증 및 출력
    ans = 0
    for decoded in done:
        if decoded:
            decoded.reverse()
            odd = 0
            even = 0
            checker = decoded[-1]
            for i in range(4):
                odd += decoded[2*i]*3
            for j in range(3):
                even += decoded[2*j+1]
            value = odd + even + checker
            if value % 10 == 0:
                ans += sum(decoded)
    print(f"#{tc} {ans}")
