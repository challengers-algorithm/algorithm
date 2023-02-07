# https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 베스트 알고리즘: 수학

def solution(x):
    return x % sum(map(int, list(str(x)))) == 0