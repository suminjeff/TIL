def time(date):
    year, month, day = map(int, date.split("."))
    return year*12*28 + month*28 + day


def solution(today, terms, privacies):
    answer = []
    today = time(today)
    for idx, privacy in enumerate(privacies):
        start_date, term_type = privacy.split()
        start_date = time(start_date)
        for term in terms:
            term_policy, duration = term.split()
            duration = int(duration) * 28
            if term_type == term_policy and start_date + duration <= today:
                answer.append(idx+1)

    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))