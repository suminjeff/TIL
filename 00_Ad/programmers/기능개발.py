def solution(progresses, speeds):
    N = len(progresses)
    answer = []
    front = -1
    rear = N - 1
    done = 0

    while done < N:
        cnt = 0
        if progresses[front + 1] >= 100:
            cnt += 1
            done += 1
            front += 1
            for i in range(front + 1, rear+1):
                if progresses[i] >= 100:
                    cnt += 1
                    done += 1
                    front += 1
                else:
                    break
        else:
            for i in range(N):
                if progresses[i] >= 100:
                    continue
                progresses[i] += speeds[i]
        if cnt:
            answer.append(cnt)

    return answer


progresses1 = [93, 30, 55]
progresses2 = [95, 90, 99, 99, 80, 99]

speeds1 = [1, 30, 5]
speeds2 = [1, 1, 1, 1, 1, 1]

ans1 = solution(progresses1, speeds1)
ans2 = solution(progresses2, speeds2)
print(ans1)
print(ans2)