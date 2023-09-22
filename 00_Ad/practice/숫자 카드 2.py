import sys
sys.stdin = open("숫자 카드 2.txt", "r")
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cd = {}
for card in cards:
    if card in cd.keys():
        cd[card] += 1
    else:
        cd[card] = 1
M = int(input())
checker = list(map(int, input().split()))
for check in checker:
    ans = cd.get(check)
    print(0 if ans is None else ans, end=" ")