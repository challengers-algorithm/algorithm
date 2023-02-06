# https://school.programmers.co.kr/learn/courses/30/lessons/12907
# 예상 알고리즘: DP
# 베스트 알고리즘: DP

# 거스름돈 문제를 그리디로 풀려면 큰 단위가 작은 단위의 배수여야 한다.
# 이 문제는 큰 단위가 작은 단위의 배수가 아니다. => 그리디 X
# 따라서 DP로 접근한다.

def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1
    money.sort()
    for m in money:
        for i in range(m, n+1):
            dp[i] += dp[i-m]
    return dp[-1]


print(solution(5, [1, 2, 5]))
# 4
