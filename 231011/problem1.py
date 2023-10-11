import sys
sys.stdin = open("problem1.txt", "r")
input = sys.stdin.readline
from collections import deque


def distance(r, c, EXIT):
    return abs(r-EXIT[0]) + abs(c-EXIT[1])


def turn90(rectangle):
    global EXIT
    r, c, length = rectangle
    turned_rectangle = [[0]*N for _ in range(N)]
    exit_and_person = [[0]*N for _ in range(N)]
    exit_and_person[EXIT[0]][EXIT[1]] = "EXIT"
    for pr, pc in people:
        exit_and_person[pr][pc] = "PERSON"
    turned_exit_and_person = [[0]*N for _ in range(N)]
    for i in range(r, r+length):
        for j in range(c, c+length):
            if [i, j] in people:
                people.remove([i, j])
            turned_exit_and_person[j][length-i-1] = exit_and_person[i][j]
            turned_rectangle[j][length-i-1] = arr[i][j] - 1 if arr[i][j] - 1 >= 0 else 0
    for i in range(r, r+length):
        for j in range(c, c+length):
            arr[i][j] = turned_rectangle[i][j]
            if turned_rectangle[i][j] == "EXIT":
                EXIT = [i, j]
            elif turned_rectangle[i][j] == "PERSON":
                people.append([i, j])

def find_closest_person(EXIT):
    r, c = EXIT
    visited = [[0]*N for _ in range(N)]
    visited[r][c] = 1
    que = deque()
    que.append([r, c, 0])
    while que:
        r, c, d = que.popleft()
        if [r, c] in people:
            return [r, c]
        for dr, dc in find_closest_delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = 1
                que.append([nr, nc, d+1])


def find_smallest_rectangle(EXIT, person):
    length = max(abs(EXIT[0]-person[0]), abs(EXIT[1]-person[1])) + 1
    # 좌상
    if EXIT[0] >= person[0] and EXIT[1] >= person[1]:
        idx = 0
    # 우상
    elif EXIT[0] >= person[0] and EXIT[1] <= person[1]:
        idx = 1
    # 좌하
    elif EXIT[0] <= person[0] and EXIT[1] >= person[1]:
        idx = 2
    # 우하
    # elif EXIT[0] <= person[0] and EXIT[1] <= person[1]:
    else:
        idx = 3
    r, c = EXIT
    dr, dc = find_smallest_delta[idx]
    for _ in range(length-1):
        nr, nc = r + dr, c + dc
        if 0 <= nr < N:
            r = nr
        if 0 <= nc < N:
            c = nc
    return [r, c, length]


find_smallest_delta = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
find_closest_delta = [[-1, 0], [0, -1], [0, 1], [1, 0]]
moving_delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
people = deque()
for _ in range(M):
    pr, pc = map(int, input().split())
    people.append([pr-1, pc-1])
EXIT = list(map(int, input().split()))
EXIT[0] -= 1
EXIT[1] -= 1

cnt = 0
while people:
    if K == 0:
        break

    # 이동
    for _ in range(len(people)):
        r, c = people.popleft()
        flag = False
        for dr, dc in moving_delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
                if [nr, nc] == EXIT:
                    flag = True
                    break
                else:
                    if distance(r, c, EXIT) > distance(nr, nc, EXIT):
                        cnt += 1
                        people.append([nr, nc])
                        flag = True
                        break
        if not flag:
            people.append([r, c])
    # 회전
    person = find_closest_person(EXIT)
    rectangle = find_smallest_rectangle(EXIT, person)
    turn90(rectangle)
    # 시간 빼기
    K -= 1

print(cnt)
print(EXIT)

