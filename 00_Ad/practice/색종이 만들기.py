import sys
sys.stdin = open('색종이 만들기.txt', 'r')
input = sys.stdin.readline


def divide(length, r_start, r_end, c_start, c_end):
    if length == 1:
        if not visited[r_start][c_start]:
            cnt[arr[r_start][c_start]] += 1
            visited[r_start][c_start] = 1
        return
    if conquer(r_start, r_end, c_start, c_end):
        cnt[arr[r_start][c_start]] += 1
        return
    r_middle, c_middle = (r_start+r_end)//2, (c_start+c_end)//2
    divide(length//2, r_start, r_middle, c_start, c_middle)
    divide(length//2, r_middle, r_end, c_middle, c_end)
    divide(length//2, r_start, r_middle, c_middle, c_end)
    divide(length//2, r_middle, r_end, c_start, c_middle)


def conquer(r_start, r_end, c_start, c_end):
    v = arr[r_start][c_start]
    for r in range(r_start, r_end):
        for c in range(c_start, c_end):
            if arr[r][c] != v:
                return False
    for r in range(r_start, r_end):
        for c in range(c_start, c_end):
            visited[r][c] = 1
    return True


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = {
    0: 0,
    1: 0,
}
# print(*arr, sep="\n")
divide(N, 0, N, 0, N)
print(cnt[0])
print(cnt[1])
# print(*visited, sep="\n")
