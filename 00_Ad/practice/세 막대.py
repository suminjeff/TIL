import sys
sys.stdin = open("세 막대.txt", "r")

arr = list(map(int, input().split()))
m = max(arr)
if m - (sum(arr) - m) >= 0:
    i = arr.index(m)
    while arr[i] - (sum(arr) - arr[i]) >= 0:
        arr[i] -= 1
    print(sum(arr))
else:
    print(sum(arr))