import sys

sys.stdin = open("가장 빠른 문자열 타이핑.txt", "r", encoding="utf-8")


def my_len(arr):
    cnt = 0
    for a in arr:
        cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    t, p = input().split()
    t_len = my_len(t)
    p_len = my_len(p)
    t_idx = 0
    p_idx = 0
    cnt = 0

    while t_idx < t_len:
        if t[t_idx] == p[p_idx]:
            t_idx += 1
            p_idx += 1
            if p_idx == p_len - 1:
                cnt += 1
                p_idx = 0
        else:
            t_idx = t_idx - p_idx + 1
            p_idx = 0
    ans = t_len - p_len*cnt + cnt
    print(f"#{tc} {ans}")
