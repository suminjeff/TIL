import sys

sys.stdin = open("베이비진 게임.txt", "r")


def check(card_set):
    card_set.sort()
    triplet = []
    top = -1
    for card in card_set:
        if triplet:
            if triplet[top] == card:
                triplet.append(card)
                if len(triplet) == 3:
                    return True
            else:
                triplet.clear()
                triplet.append(card)
                top = 0
        else:
            triplet.append(card)
            top += 1

    baby_run = []
    top = -1
    for card in card_set:
        if baby_run:
            if baby_run[top] + 1 == card:
                baby_run.append(card)
                top += 1
                if len(baby_run) == 3:
                    return True
            else:
                if baby_run[top] == card:
                    continue
                else:
                    baby_run.clear()
                    baby_run.append(card)
                    top = 0
        else:
            baby_run.append(card)
            top += 1
    return False


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    player1_deck = []
    player2_deck = []
    winner = 0
    for i in range(6):
        player1 = arr[2*i]
        player1_deck.append(player1)
        if len(player1_deck) > 2:
            if check(player1_deck):
                winner = 1
                break

        player2 = arr[2*i+1]
        player2_deck.append(player2)
        if len(player2_deck) > 2:
            if check(player2_deck):
                winner = 2
                break
    print(f"#{tc} {winner}")