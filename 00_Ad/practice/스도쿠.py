import sys
sys.stdin = open("스도쿠.txt", "r")
input = sys.stdin.readline



board = [list(map(int, input().split())) for _ in range(9)]

for row in range(9):
    for col in range(9):
        if board[row][col] == 0:

