import sys

sys.stdin = open("영화감독 숌.txt", "r")


N = int(input())

que = ['666']
cnt = 1

while cnt != N:
    num = que.pop(0)
    min_num = float('inf')
    for i in range(10):
        if i == 0:
            tmp_num = int(num+str(i))
            min_num = min(min_num, tmp_num)
        else:
            tmp_num1 = int(str(i)+num)
            tmp_num2 = int(num+str(i))
            min_num = min(min_num, tmp_num1, tmp_num2)
    que.append(str(min_num))
    cnt += 1
print(*que)