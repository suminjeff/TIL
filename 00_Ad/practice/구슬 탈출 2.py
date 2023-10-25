import sys

sys.stdin = open('구슬 탈출 2.txt', 'r')
input = sys.stdin.readline

from copy import deepcopy

# 각각의 동작에서 공은 동시에 움직인다
# 빨간 구슬이 구멍에 빠지면 성공이지만 파란 구슬이 구멍에 빠지면 실패다
# 빨간 구슬과 파란 구슬이 동싱에 구멍에 빠져도 실패다
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다
# 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다
# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다

# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하기


def backtrack(depth, past_direction):
    global min_depth
    global board
    print(">>>>>>", depth, past_direction)
    print(*board, sep="\n")
    print(goal_in)
    print()
    if depth >= min_depth:
        return
    if depth >= 10:
        if goal_in["R"] is True and goal_in["B"] is False:
            min_depth = min(min_depth, depth)
        return
    if goal_in["R"] is True and goal_in["B"] is False:
        min_depth = min(min_depth, depth)
        return
    red_pos, blue_pos = position["R"], position["B"]
    red_goal, blue_goal = goal_in["R"], goal_in["B"]
    for direction in range(4):
        if direction != past_direction:
            turn(direction)
            backtrack(depth + 1, direction)
            # reset(red_pos, blue_pos, position["R"], position["B"], red_goal, blue_goal)
            # goal_in["R"], goal_in["B"] = red_goal, blue_goal


# 0: 왼쪽, 1: 오른쪽, 2: 위쪽, 3: 아래쪽
def turn(direction):
    rr, rc = position["R"]
    br, bc = position["B"]
    board[rr][rc] = board[br][bc] = "."
    marbles = [[rr, rc, "R"], [br, bc, "B"]]
    if direction == 0:
        marbles.sort(key=lambda x: x[1])
    elif direction == 1:
        marbles.sort(key=lambda x: x[1], reverse=True)
    elif direction == 2:
        marbles.sort(key=lambda x: x[0])
    elif direction == 3:
        marbles.sort(key=lambda x: x[0], reverse=True)
    for r, c, color in marbles:
        while board[r][c] == ".":
            r, c = r + delta[direction][0], c + delta[direction][1]
            if board[r][c] == "O":
                goal_in[color] = True
                position[color] = [r, c]
                break
        if not goal_in[color]:
            r, c = r - delta[direction][0], c - delta[direction][1]
            board[r][c] = color
            position[color] = [r, c]


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
delta = [[0, -1], [0, 1], [-1, 0], [1, 0]]
position = {}
goal_in = {"R": False, "B": False}
min_depth = 11
for i in range(N):
    for j in range(M):
        v = board[i][j]
        if v == "R":
            position.setdefault("R", [i, j])
        elif v == "B":
            position.setdefault("B", [i, j])
        elif v == "O":
            position.setdefault("H", [i, j])

# backtrack(0, -1)
# print(min_depth)

turn(0)
print(*board, sep="\n")
print()
turn(3)
print(*board, sep="\n")
print()
