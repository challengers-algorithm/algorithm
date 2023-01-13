# https://school.programmers.co.kr/learn/courses/30/lessons/12945
# 예상 알고리즘: DP
# 베스트 알고리즘: 
import sys
sys.setrecursionlimit(10**8)
dp = {1: 1, 2: 1}
def solution(n):
    if n in dp:
        return dp[n]
    dp[n] = (solution(n-2) + solution(n-1)) % 1234567
    return dp[n]    
    

print(solution(3)) # 2
