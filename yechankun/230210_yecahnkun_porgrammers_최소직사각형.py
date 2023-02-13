# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 베스트 알고리즘: 정렬

def solution(sizes):
    sizesT = list(zip(*[sorted(i) for i in sizes]))
    return max(sizesT[0]) * max(sizesT[1])