def solution(priorities, location):
    for i, p in enumerate(priorities):
        priorities[i] = [p, i]
    done = []
    while priorities:
        max_p = max(priorities)
        cur = priorities.pop(0)
        if cur[0] != max_p[0]:
            priorities.append(cur)
        else:
            done.append(cur)

    for i in range(len(done)):
        if done[i][1] == location:
            return i+1
    # for i in range(len(done)):
    #     if done[i] == location:
    #         return i


priorities1 = [2, 1, 3, 2]
location1 = 2

priorities2 = [1, 1, 9, 1, 1, 1]
location2 = 0

print(solution(priorities1, location1))
print(solution(priorities2, location2))
