import sys

sys.stdin = open("숫자 카드.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    cards = input()
    counts = [0] * 10

    max_count = 0
    mode = 0

    for i in cards:
        counts[int(i)] += 1

    for i in range(10):
        if max_count <= counts[i]:
            max_count = counts[i]
            mode = i

    print(f"#{tc} {mode} {max_count}")