N = 5; M = 8; K = 3
arr = [2, 4, 5, 4, 6]
n1 = max(arr)
arr.remove(n1)
n2 = max(arr)
multiply = M//K*2
additional = M % K*2

ans = (n1+n2) * multiply + n1 * additional
print(ans)