import sys
sys.stdin = open('게리멘더링 2.txt', 'r')
input = sys.stdin.readline


# 꼭지점 정하기
def point(n):
    global min_v
    for x in range(n-2):
        for y in range(1, n-1):
            for d1 in range(1, n-1):
                for d2 in range(1, n-1):
                    if (0 <= x+d1 < N and 0 <= y-d1 < N) and (0 <= x+d2 < N and 0 <= y+d2 < N):
                        v = divide(x, y, d1, d2)
                        min_v = min(min_v, v)



def divide(x, y, d1, d2):
    section = [0]*5
    for r in range(N):
        for c in range(N):
            section_five(x, y, d1, d2)
            # if 0 <= r < x+d1 and 0 <= c <= y:
            #     section[0] += arr[r][c]
            #     arr[r][c] = 1
            # elif 0 <= r <= x+d2 and y < c < N:
            #     section[1] += arr[r][c]
            #     arr[r][c] = 2
            # elif x+d1 <= r < N and 0 <= c < y-d1+d2:
            #     section[2] += arr[r][c]
            #     arr[r][c] = 3
            # elif x+d2 < r < N and y-d1+d2 <= c < N:
            #     section[3] += arr[r][c]
            #     arr[r][c] = 4
            # else:
            #     section[4] += arr[r][c]
            #     arr[r][c] = 5
    # print(f"x:{x}, y:{y}, d1:{d1}, d2:{d2}")
    # # print(section)
    # print(*arr, sep="\n")
    # print()
    # return max(section) - min(section)

def section_five(x, y, d1, d2):
    res = 0
    que = []
    for i in range(d1):
        for j in range(d2):
            print(i, j)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = float('inf')
# print(*arr, sep="\n")
# point(N)
section_five(1, 4, 3, 2)
# print(min_v)