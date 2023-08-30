import sys

sys.stdin = open("완전검색 연습_베이비진.txt", "r")


def check(card_set):
    triplet = []
    top = -1
    for card in card_set:
        card = int(card)
        if triplet:
            if triplet[top] == card:
                triplet.append(card)
            else:
                triplet.clear()
                triplet.append(card)
                top = 0
        else:
            triplet.append(card)
            top += 1

    run = []
    top = -1
    for card in card_set:
        card = int(card)
        if run:
            if run[top] + 1 == card:
                run.append(card)
                top += 1
            else:
                run.clear()
                run.append(card)
                top = 0
        else:
            run.append(card)
            top += 1

    if len(triplet) == 3 or len(run) == 3:
        return True
    else:
        return False


def baby_gin(cards, N):
    for i in range(1 << (N-1)):
        set1 = []
        set2 = []
        for j in range(N):
            if i & (1 << j):
                set1.append(cards[j])
            else:
                set2.append(cards[j])
        if len(set1) == 3 and len(set2) == 3:
            if check(set1) and check(set2):
                return 1
            else:
                return 0


T = int(input().strip())
for tc in range(1, T+1):
    arr = list(input().strip())
    arr.sort()
    print(f"#{tc} {baby_gin(arr, 6)}")
