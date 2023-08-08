import sys

sys.stdin = open("회문1.txt", "r", encoding="utf-8")

def my_len(arr):
    count = 0
    for a in arr:
        count += 1
    return count


def brute_force(target, pattern):
    t_idx = 0
    p_idx = 0

    t_len = my_len(target)
    p_len = my_len(pattern)
    while (t_idx < t_len) and (p_idx < p_len):
        if target[t_idx] == pattern[p_idx]:
            t_idx += 1
            p_idx += 1
        else:
            t_idx = t_idx - p_idx + 1
            p_idx = 0

    if p_idx == p_len:
        return t_idx - p_idx
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    t = input()
    p = input()
    print(brute_force(t, p))
