# https://school.programmers.co.kr/learn/courses/30/lessons/12971
# 예상 알고리즘: DP
# 베스트 알고리즘:

def calDp(dp):
    if len(dp) == 1:
        return [dp[0]]
    dp[1] = max(dp[0], dp[1] if len(dp) > 1 else 0)
    for i in range(2, len(dp)):
        dp[i] = max(dp[i-1], dp[i]+dp[i-2])
    return dp

def solution(sticker):
    L = len(sticker)
    if L == 1:
        return sticker[0]
    dp1 = calDp([sticker[i] for i in range(L-1)])
    dp2 = calDp([sticker[i] for i in range(1, L)])
    return max(dp1[-1], dp2[-1])

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
print(solution([1, 3]))
