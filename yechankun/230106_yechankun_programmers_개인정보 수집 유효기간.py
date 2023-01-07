# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 예상 알고리즘: 구현
# 베스트 알고리즘: 구현


def solution(today, terms, privacies):
    today = dateStrToInt(today)
    termsDict = {}
    for item in terms:
        kind, term = item.split()
        termsDict[kind] = int(term)*28

    answer = []
    for i, item in enumerate(privacies, 1):
        date, kind = item.split()
        date = dateStrToInt(date)
        if isDelete(today, date, termsDict[kind]):
            answer.append(i)
    return answer


def isDelete(today, joinDate, term):
    if today >= joinDate + term:
        return True
    return False


MONTH_DAY = 28
YEAR_DAY = MONTH_DAY*12


def dateStrToInt(date):
    year, month, day = map(int, date.split('.'))
    return year*YEAR_DAY + (month-1)*MONTH_DAY + day


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], [
      "2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
