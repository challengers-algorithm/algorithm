# https://school.programmers.co.kr/learn/courses/30/lessons/12934
# 베스트 알고리즘: 수학

def solution(n):   
    return int(n**0.5+1) ** 2 if n**0.5 == int(n**0.5) else -1