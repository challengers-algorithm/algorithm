# https://school.programmers.co.kr/learn/courses/30/lessons/12914
# 예상 알고리즘: 수학, 조합
# 베스트 알고리즘: 수학, DP, 피보나치 수열

fact = [1] * 2001
fact[1] = 1
for i in range(2, 2001):
    fact[i] = fact[i-1]*i

def nCr(n, r):
    return fact[n] // (fact[n-r] * fact[r])

def solution(n):  
    answer = 0
    for i in range(n):
        if n-i < i:
            break
        answer += nCr(n-i, i)
    return answer % 1234567

# 4C2, 3C1
print(solution(4))
print(solution(3))
print(solution(2000))
print(solution(1999))

# n=4
# 4 0
# 3 1
# 2 2

# n=5
# 5 0
# 4 1
# 3 2
# 2 3
