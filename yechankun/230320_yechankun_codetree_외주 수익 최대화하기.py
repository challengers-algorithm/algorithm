# https://www.codetree.ai/training-field/frequent-problems/max-of-outsourcing-profit
# 예상 알고리즘: 백트래킹
# 베스트 알고리즘: 백트래킹, dp

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def solutionInput():
    n = int(input())
    works = [list(map(int, input().split())) for _ in range(n)]
    return n, works

def solution(n, works):    
    answer = dfs(0, 0, n, works)
    return answer

# 조합과 dfs와 같은 picker 방식을 이용해서
# 백트래킹을 시도해보자

def dfs(curr, totalP, n, works):
    answer = totalP
    for i in range(curr, n):
        t, p = works[i]
        if i + t < n:
            answer = max(answer, dfs(i + t, totalP + p, n, works))
        elif i + t == n:
            answer = max(answer, totalP + p)
    return answer

print(solution(*solutionInput()))