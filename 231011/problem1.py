import sys
sys.stdin = open("problem1.txt", "r")
input = sys.stdin.readline
from collections import deque


def distance(r, c, EXIT):
    return abs(r-EXIT[0]) + abs(c-EXIT[1])


def turn90(rectangle):
    global EXIT
    r, c, length = rectangle
    turned = [[0]*N for _ in range(N)]
    stack = []
    for i in range(r, r+length):
        for j in range(c, c+length):
            v = arr[i][j]
            if v == "PERSON":
                people.remove([i, j])
            elif type(v) == int and v > 0:
                v -= 1
            stack.append(v)
    for j in range(c+length-1, c-1, -1):
        for i in range(r, r+length):
            turned[i][j] = stack.pop(0)

    for i in range(r, r+length):
        for j in range(c, c+length):
            arr[i][j] = turned[i][j]
            if turned[i][j] == "EXIT":
                EXIT = [i, j]
            elif turned[i][j] == "PERSON":
                people.append([i, j])


def find_closest_person(EXIT):
    r, c = EXIT
    visited = [[0]*N for _ in range(N)]
    visited[r][c] = 1
    que = deque()
    que.append([r, c, 0])
    while que:
        r, c, d = que.popleft()
        if arr[r][c] == 'PERSON':
            return [r, c]
        for dr, dc in find_closest_delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = 1
                que.append([nr, nc, d+1])


def find_smallest_rectangle(EXIT, person):
    length = max(abs(EXIT[0]-person[0]), abs(EXIT[1]-person[1])) + 1
    for i in range(N):
        for j in range(N):
            isExit = False
            isPerson = False
            for si in range(i, i+length):
                for sj in range(j, j+length):
                    if [si, sj] == EXIT:
                        isExit = True
                    elif [si, sj] == person:
                        isPerson = True
            if isExit and isPerson:
                return [i, j, length]


find_smallest_delta = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
find_closest_delta = [[-1, 0], [0, -1], [0, 1], [1, 0]]
moving_delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
people = deque()
for _ in range(M):
    pr, pc = map(int, input().split())
    people.append([pr-1, pc-1])
    arr[pr-1][pc-1] = 'PERSON'
    print(pr-1, pc-1, arr[pr-1][pc-1])
EXIT = list(map(int, input().split()))
EXIT[0] -= 1
EXIT[1] -= 1
arr[EXIT[0]][EXIT[1]] = 'EXIT'
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
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 'PERSON' or arr[nr][nc] == 'EXIT' or arr[nr][nc] == 0:
                    if arr[nr][nc] == 'EXIT':
                        if arr[r][c] == 'PERSON':
                            cnt += 1
                            arr[r][c] = 0
                        flag = True
                        break
                    else:
                        if (distance(r, c, EXIT) > distance(nr, nc, EXIT)) and arr[nr][nc] == 0:
                            if arr[r][c] == 'PERSON':
                                arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]
                            cnt += 1
                            people.append([nr, nc])
                            flag = True
                            break
        if not flag:
            people.append([r, c])
    # 회전
    person = find_closest_person(EXIT)
    rectangle = find_smallest_rectangle(EXIT, person)
    print("person :", person, "rectangle :", rectangle)
    print("people :", people)
    print("before :", *arr, sep="\n")
    print("TURN")
    turn90(rectangle)
    print("people :", people)
    print("after :", *arr, sep="\n")
    print()
    print()
    # 시간 빼기
    K -= 1

print(cnt)
print(EXIT[0]+1, EXIT[1]+1)

