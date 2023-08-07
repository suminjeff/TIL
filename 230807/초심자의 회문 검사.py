import sys
sys.stdin = open("초심자의 회문 검사.txt", "r")

T = int(input())
for tc in range(1, T+1):
    word = input()
    ans = 0
    if word == word[::-1]:
        ans = 1

    print(f"#{tc} {ans}")