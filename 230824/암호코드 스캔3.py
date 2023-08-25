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
    arr = [input() for _ in range(N)]
    vstd = [[0]*M for _ in range(N)]
    bicodes = []
    for row in range(N):
        for col in range(M):
            if arr[row][col] != "0" and not vstd[row][col]:
                v = arr[row][col]
                vstd[row][col] = 1
                hexcode = ""
                bicode = ""
                
                # 행의 범위 찾기
                r = row
                while r < N:
                    if arr[r][col] == v:
                        r += 1
                    else:
                        break
                
                # 열의 범위와 암호 찾기
                c = col
                while c < M:
                    if arr[row][c] != "0":
                        hexcode += arr[row][c]
                        c += 1
                    else:
                        for hex in hexcode:
                            bicode += bin(int(hex, 16)).lstrip("0b").zfill(4)
                        bicode = bicode.rstrip("0")
                        c += 1
                        # if len(bicode) % 7 != 0:
                        #     hexcode += arr[row][c]
                        #     c += 1
                        # else:
                        #     bicodes.append(bicode)
                        #     break
            else:
                vstd[row][col] = 1
                continue