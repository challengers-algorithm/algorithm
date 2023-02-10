# https://school.programmers.co.kr/learn/courses/30/lessons/12943
# 베스트 알고리즘: 수학

def solution(num):
    answer = 0
    for _ in range(500):
        if num == 1:
            return answer
        num = num//2 if num%2==0 else num*3 + 1
        answer += 1
    return -1