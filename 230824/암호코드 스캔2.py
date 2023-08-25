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

    # 2진수 4개 묶음을 하나로 합치기
    bi_arr = []
    for r in range(N):
        temp = "".join(arr[r])
        bi_arr.append(temp)
    # print(temp_list)
    # 없으면 몇배인지 확인하고 그 배수만큼 56을 곱한 값을 탐색

    # 2진수 행방향 거꾸로 보면서 1 찾으면 아래로 범위 확인,
    need_check = []
    done = []
    vstd = [[0]*M*4 for _ in range(N)]
    for row in range(N):
        col = M*4 - 1
        de_code = []
        if bi_arr[row].count("0") == M*4:
            continue
        else:
            while col >= 0:
                # 행을 거꾸로 보면서 첫번째 암호(거꾸로 보니까 검증코드일 것)의 비율 확인
                if bi_arr[row][col] == "1" and not vstd[row][col]:
                    vstd[row][col] = 1
                    one_zero = "1"
                    ratio_check = []
                    div_cnt = 1
                    temp_col = col
                    temp_row = row
                    row_cnt = 0
                    while temp_row < N:
                        if bi_arr[temp_row][col] == "1":
                            vstd[temp_row][col] = 1
                            temp_row -= 1
                            row_cnt += 1
                        else:
                            break
                    print(row_cnt)
                    # 비율 확인
                    for _ in range(3):
                        cnt = 0
                        if bi_arr[row][temp_col] == one_zero:
                            while bi_arr[row][temp_col] == one_zero:
                                cnt += 1
                                temp_col -= 1
                            one_zero = str(1 - int(one_zero))
                            ratio_check.append(cnt)

                    # 비율 확인 작업
                    # 비율이 BP_ratio에 있으면 진행
                    # 없으면 2로 계속 나누기
                    if 1 not in ratio_check:
                        divide = 2
                        while True:
                            for i in range(3):
                                ratio_check[i] //= divide
                            div_cnt += 1
                            if 1 in ratio_check:
                                break
                    ratio_check = tuple(ratio_check)
                    if ratio_check in BP_ratio:
                        done.append(BP_ratio[ratio_check][0])
                    col -= 7*div_cnt

                    # else:
                    #     col -= 56*div_cnt

                else:
                    vstd[row][col] = 1
                    col -= 1
    print(done)


        # #             if 1 in ratio_check:
        # #                 ratio_check = tuple(ratio_check)
        # #             if ratio_check in BP_ratio:
        # #                 code_block_to_dec.append(BP_ratio[ratio_check][0])
        # #             # else:
        # #             #     break
    #     if len(code_block_to_dec) > 8:
    #         need_check.append(code_block_to_dec)
    #     else:
    #         done.append(code_block_to_dec)
    #
    # # 확인이 필요한 코드라면
    # if need_check:
    #     temp_check_set = set()
    #     for n in need_check:
    #         for chop in range(0, len(n)-1, 8):
    #             temp_check = []
    #             for i in range(chop, chop+8):
    #                 temp_check.append(n[i])
    #             if temp_check not in done:
    #                 done.append(temp_check)

    # 해독 암호 검증 및 출력
    # ans = 0
    # for decoded in done:
    #     if decoded:
    #         decoded.reverse()
    #         odd = 0
    #         even = 0
    #         checker = decoded[-1]
    #         for i in range(4):
    #             odd += decoded[2*i]*3
    #         for j in range(3):
    #             even += decoded[2*j+1]
    #         value = odd + even + checker
    #         if value % 10 == 0:
    #             ans += sum(decoded)
    # print(f"#{tc} {ans}")
