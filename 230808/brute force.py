def my_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

def brute_force(t, p):
    t_idx = 0
    p_idx = 0

    t_len = len(t)
    p_len = len(p)

    while t_idx < t_len and p_idx < p_len:
        if t[t_idx] == p[p_idx]:
            t_idx += 1
            p_idx += 1
        else:
            t_idx = t_idx - p_idx + 1
            p_idx = 0

    if p_idx == p_len:
        return t_idx - p_idx
    else:
        return -1