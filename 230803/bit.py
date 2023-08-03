def print_subset(bit, arr, n):
    total = 0  # 부분집합의 합
    for i in range(n):
        if bit[i]:
            print(arr[i], end=' ')
            total += arr[i]
    print(bit, total)


n = 4
arr = [1, 2, 3, 4]
bit = [0] * n

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                # print_subset(bit, arr, 4)

for i in range(1 << n):
    bit[0] = i
    for j in range(n):
        bit[1] = j
        if i & (1 << j):
            print(arr[j], end=", ")
    print()
print()
