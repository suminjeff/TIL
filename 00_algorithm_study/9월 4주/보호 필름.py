import sys

sys.stdin = open("보호 필름.txt", "r")


def test():
    for c in range(W):
        stack = []
        cnt = 0
        flag = False
        for r in range(D):
            v = arr[r][c]
            if stack:
                if stack[-1] == v:
                    stack.append(v)
                    cnt += 1
                    if cnt >= K:
                        flag = True
                        break
                else:
                    stack.clear()
                    stack.append(v)
                    cnt = 1
            else:
                stack.append(v)
                cnt += 1
        if not flag:
            return False
    return True


def dfs(d, array, visited):
    global min_d
    if test():
        d -= 1
        min_d = min(min_d, d)
        return
    elif d >= min_d:
        return
    for j in range(D):
        for k in range(1):
            if not visited[j]:
                visited[j] = 1
                array[j] = [k] * W
                dfs(d+1, array, visited)




T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    if test():
        print(f"#{tc} {0}")
    else:
        min_d = D
        visited = [0] * D
        dfs(0, arr, visited)
        print(f"#{tc} {min_d}")

