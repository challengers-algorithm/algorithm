# https://school.programmers.co.kr/learn/courses/30/lessons/131128
# 예상 알고리즘: 해싱
# 베스트 알고리즘: 해싱

from collections import Counter
def solution(X, Y):
    answer = ''
    yCounter = Counter(Y)
    for x in sorted(X, reverse=True):
        if yCounter[x] > 0:
            yCounter[x] -= 1
            answer+=x
    answer = ('0' if answer[0] == '0' else answer) if answer else '-1'
    return answer