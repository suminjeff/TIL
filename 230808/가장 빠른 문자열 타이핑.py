import sys

sys.stdin = open("가장 빠른 문자열 타이핑.txt", "r", encoding="utf-8")


def my_len(arr):
    count = 0
    for a in arr:
        count += 1
    return count


def brute_force(t, p):
    t_idx = 0
    p_idx = 0

    t_len = my_len(t)
    p_len = my_len(p)

    checklist = []
    while t_idx < t_len and p_idx < p_len:
        if t[t_idx] == p[p_idx]:
            t_idx += 1
            p_idx += 1
        else:
            t_idx = t_idx - p_idx + 1
            p_idx = 0

    if p_idx == p_len:
        checklist.append(t_idx - p_idx)
    else:
        return False
    return checklist


T = int(input())
for tc in range(1, T+1):
    t, p = input().split()
    start = 0
    check_list = brute_force(t, p)
    while start < my_len(t):
