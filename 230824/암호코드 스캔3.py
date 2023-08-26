import sys

sys.stdin = open('암호코드 스캔.txt', 'r')


def hex_to_bin(hex_str):
    bin_str = ""
    for h in hex_str:
        bin_str += f"{int(h, base=16):04b}"
    return bin_str


def get_width(row):
    count = 0
    end_point = 0
    before = "0"
    change = 0



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
    hexcodes = []
    for row in range(N):
        for col in range(M):
            if arr[row][col] != "0":
                end_r = 0
                for r in range(N):
                    if arr[r][col] != "0":
                        end_r = r