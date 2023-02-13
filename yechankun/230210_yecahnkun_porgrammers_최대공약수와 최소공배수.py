# https://school.programmers.co.kr/learn/courses/30/lessons/12940
# 베스트 알고리즘: 수학

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def solution(n, m):
    g = gcd(n, m)
    m = n*m / g
    return [g, m]