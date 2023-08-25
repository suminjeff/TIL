import sys

sys.stdin = open('암호코드 스캔.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print(f"#{tc}")