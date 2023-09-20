import sys
from copy import deepcopy

sys.stdin = open("보호 필름.txt", "r")


def test(D, W, K, arr):
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


T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]

    if test(D, W, K, arr):
        min_cnt = 0
    else:
        min_cnt = float('inf')
        for row in range(D):
            for treatment in range(2):
                visited = [0] * D
                visited[row] = 1
                que = [[row, treatment]]
                clone = deepcopy(arr)
                cnt = 0
                while que:
                    r, t = que.pop(0)
                    clone[r] = [t] * W
                    cnt += 1
                    if test(D, W, K, clone):
                        break
                    elif cnt >= min_cnt:
                        break
                    for d in range(D):
                        if not visited[d]:
                            visited[d] = 1
                            que.append([d, 0])
                            que.append([d, 1])



                min_cnt = min(min_cnt, cnt)


                visited = [0] * D
                visited[row] = 1
                clone[row] = [treatment] * W




    print(f"#{tc} {min_cnt}")

