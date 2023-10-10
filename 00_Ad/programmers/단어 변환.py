def solution(begin, target, words):
    n = len(begin)
    m = len(words)
    visited = [0]*m
    que = [begin]
    answer = 0
    while que:
        w = que.pop(0)
        if w == target:
            return answer
        for i in range(m):
            cnt = 0
            for j in range(n):
                if w[j] != words[i][j]:
                    cnt += 1
            if cnt == 1:
                que.append(words[i])
        answer += 1


begin1 = "hit"
target1 = "cog"
words1 = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin1, target1, words1))