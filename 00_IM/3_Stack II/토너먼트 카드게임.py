import sys

sys.stdin = open("토너먼트 카드게임.txt", "r")


def winner(left, right):
    match = [arr[left], arr[right]]
    right_win = [[1, 2], [2, 3], [3, 1]]
    if match in right_win:
        return right
    else:
        return left


def tournament(start, end):
    if start == end:
        return start
    else:
        left = tournament(start, (start+end)//2)
        right = tournament((start+end)//2 + 1, end)
        return winner(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    champion = tournament(0, N-1)
    print(f"#{tc} {champion+1}")