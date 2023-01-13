# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# 예상 알고리즘: 수학
# 베스트 알고리즘: 수학

def solution(n):
    lsb = n & -n
    n_p_lsb = n+lsb
    answer = n ^ n_p_lsb
    answer //= lsb
    answer >>= 2
    answer ^= n_p_lsb
    return answer

print(solution(5))