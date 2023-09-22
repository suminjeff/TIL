import sys
sys.stdin = open("회사에 있는 사람.txt", "r")
input = sys.stdin.readline

n = int(input())
pd = {}
for _ in range(n):
    p, a = map(str, input().split())
    pd[p] = a
ans = []
for k, v in pd.items():
    if v == "enter":
        ans.append(k)
ans.sort(reverse=True)
print(*ans, sep="\n")
