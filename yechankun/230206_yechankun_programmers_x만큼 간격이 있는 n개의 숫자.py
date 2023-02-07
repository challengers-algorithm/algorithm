# https://school.programmers.co.kr/learn/courses/30/lessons/12954
# 예상 알고리즘: 수학, 조건분기
# 베스트 알고리즘: 수학

def solution(x, n):
    if x == 0 : return [0] * n
    return [i for i in range(x, x*(n+1), x)]