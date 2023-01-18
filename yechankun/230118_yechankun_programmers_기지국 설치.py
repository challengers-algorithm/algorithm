# https://school.programmers.co.kr/learn/courses/30/lessons/12979
# 예상 알고리즘: 수학
# 베스트 알고리즘: 수학

from math import ceil
# stations가 오름차순 정렬되어 있음을 활용
def solution(n, stations, w):
    answer = 0
    radius = w*2+1
    start = 1
    for pos in stations:
        left, right = pos - w - 1, pos + w + 1
        if 0 < left:
            answer += ceil((left - start+1)/radius)
        start = right
    else:
        if start <= n:
            answer += ceil((n - start+1)/radius)
    return answer




print(solution(11, [4, 11], 1)) # 3
print(solution(14, [4, 11], 1)) # 3

print(solution(16, [9], 2)) # 3