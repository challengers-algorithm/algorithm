# https://school.programmers.co.kr/learn/courses/30/lessons/12938
# 예상 알고리즘: 수학, 링크드리스트
# 베스트 알고리즘: 수학

from collections import deque
def solution(n, s):
    if n > s:
        return [-1]
    answerDeque = deque([])
    while n != 1:           
        div, remain = divmod(s, n)
        n = n - 1
        if remain:
            answerDeque.appendleft(div+1)
            s -= 1 + div
        else:
            answerDeque.appendleft(div)
            s -= div
    answerDeque.appendleft(s)
    return list(answerDeque)
