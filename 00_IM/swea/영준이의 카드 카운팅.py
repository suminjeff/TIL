import sys

sys.stdin = open("영준이의 카드 카운팅.txt", "r")


def check_cards(card_string):
    max_cnt = 13
    counts = {"S": [], "D": [], "H": [], "C": []}
    i = 0
    stack = []
    while i < len(cards):
        if cards[i].isnumeric():
            while i < len(cards):
                if cards[i].isnumeric():
                    stack.append(cards[i])
                    i += 1
                else:
                    break
            card_type = stack.pop(0)
            if int("".join(stack)) in counts[card_type]:
                return ["ERROR"]
            else:
                counts[card_type].append(int("".join(stack)))
                stack.clear()
        else:
            stack.append(cards[i])
            i += 1
    ans = []
    for shape in counts:
        ans.append(max_cnt - len(counts[shape]))
    return ans


T = int(input())
for tc in range(1, T+1):
    cards = list(input())
    ans = check_cards(cards)
    print(f"#{tc}", *ans)