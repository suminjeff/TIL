import sys
sys.stdin = open("인사성 밝은 곰곰이.txt", "r")
input = sys.stdin.readline

N = int(input())
log_dict = {}
cnt = 0
for _ in range(N):
    log = input().rstrip()
    if log == "ENTER":
        log_dict = {}
    else:
        if log not in log_dict.keys():
            cnt += 1
            log_dict.setdefault(log, 1)

print(cnt)