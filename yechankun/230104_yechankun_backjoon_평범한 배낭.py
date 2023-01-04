# https://www.acmicpc.net/problem/12865
# 예상 알고리즘: DP
# 베스트 알고리즘: DP, 백트래킹, 분기한정법

from collections import defaultdict
import sys
input = sys.stdin.readline

# 입력
def solutionInput():
    N, K = map(int, input().split())
    weightPrices = [[0,0]]+[tuple(map(int, input().split())) for _ in range(N)]
    return N, K, weightPrices

# KnapSack Problem
def solution(N, K, weightPrices: defaultdict[list]):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(1, N+1):
        for j in range(1, K+1):
            weight, value = weightPrices[i]

            if weight > j:
                dp[i][j] = dp[i-1][j]
                continue
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
    return dp[N][K]

print(solution(*solutionInput()))