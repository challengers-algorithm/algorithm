# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# 예상 알고리즘: 수학
# 베스트 알고리즘: 수학

def solution(n):
    answer = 1
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 1:
            answer += 1

    return answer


print(solution(30))