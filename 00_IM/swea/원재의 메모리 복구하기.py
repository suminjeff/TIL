import sys
sys.stdin = open("원재의 메모리 복구하기.txt")
# input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    memory = input()

    print(f"#{tc} {memory}")