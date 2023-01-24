# https://school.programmers.co.kr/learn/courses/30/lessons/87390
# 예상 알고리즘: 구현, 수학
# 베스트 알고리즘: 수학
def solution(n, left, right):
    answer = [0] * (right + 1- left)
    for i in range(len(answer)):
        answer[i] = max((i + left) % n, (i + left) // n) + 1
    return answer

print(solution(3, 2, 5))
# [3,2,2,3]

print(solution(4, 7, 14))
# [4,3,3,3,4,4,4,4]

print(solution(5, 12, 21))

