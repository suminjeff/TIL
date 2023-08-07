s = 'Reverse'
s_lst = list(s)
N = len(s)
for i in range(N//2):
    s_lst[i], s_lst[N-1-i] = s_lst[N-1-i], s_lst[i]
print(''.join(s_lst))