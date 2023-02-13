# https://school.programmers.co.kr/learn/courses/30/lessons/147355
# 예상 알고리즘: 슬라이딩 윈도우
# 베스트 알고리즘: 슬라이딩 윈도우

from collections import deque
def solution(t, p):
    L = len(p)
    P = int(p)
    right = L
    slidingWindow = deque(t[:right])

    answer = 0
    for _ in range(len(t) - L):
        if int(''.join(slidingWindow)) <= P:
            answer += 1

        slidingWindow.popleft()
        slidingWindow.append(t[right])
        right += 1
    if int(''.join(slidingWindow)) <= P:
            answer += 1    
    return answer