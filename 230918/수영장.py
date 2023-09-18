import sys

sys.stdin = open("수영장.txt", "r")


T = int(input())
for tc in range(1, T + 1):
    # 0 = 1일, 1 = 1달, 2 = 3달, 3 = 1년
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_payment = [0] * 12

    # 1년짜리
    annual_fee = fee[3]
    i = 0
    
    # 3개월권 안쓰는 경우
    for i in range(12):
        if plan[i]:
            daily, monthly = plan[i] * fee[0], fee[1]
            min_payment[i] += min(daily, monthly)
    # 3개월권 쓰는 경우
    m = 0
    quarters = []
    while m < 12:
        q_sum = 0
        for i in range(m, m+3):
            if i < 12:
                q_sum += min_payment[i]
        if q_sum > fee[2]:
            quarters.append([m, m+1, m+2])
        m += 1
    if quarters:
        compare = []
        for quarter in quarters:
            used = [0] * 12
            for q in quarter:
                if q < 12:
                    used[q] = 1
            for combination in quarters:
                if quarter == combination:
                    continue
                else:
                    cnt = 0
                    for month in combination:
                        if month < 12:
                            if used[month] == 0:
                                cnt += 1
                            else:
                                break
                        else:
                            cnt += 1
                    if cnt == 3:
                        for month in combination:
                            if month < 12:
                                used[month] = 1
            potential_fee = 0
            u = 0
            while u < 12:
                if used[u] == 1:
                    potential_fee += fee[2]
                    u += 3
                else:
                    potential_fee += min_payment[u]
                    u += 1
            compare.append(potential_fee)


        ans = min(compare)
        print(f"#{tc} {min(ans, annual_fee)}")

    else:
        ans = min(sum(min_payment), annual_fee)
        print(f"#{tc} {ans}")
