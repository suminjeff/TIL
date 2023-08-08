arr = list('racecar')
N = len(arr)

ans = True
for i in range(0, N//2 - 1):
    if arr[i] != arr[N-1-i]:
        ans = False

print(ans)