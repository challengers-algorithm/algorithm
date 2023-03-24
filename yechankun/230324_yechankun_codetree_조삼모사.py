# https://www.codetree.ai/training-field/frequent-problems/three-at-dawn-and-four-at-dusk
# 예상 알고리즘: 조합, 백트래킹
# 베스트 알고리즘: 조합, DFS, 백트래킹

import sys
input = sys.stdin.readline

def solution_input():
    n = int(input())
    pij = [list(map(int, input().split())) for _ in range(n)]
    return n, pij

from itertools import combinations as comb

def solution(n, pij):
    answer = float('inf')

    # 미리 일의 합 계산
    for i in range(n):
        for j in range(n):
            pij[i][j] += pij[j][i]

    works = set(range(1, n+1))
    picks = comb(range(1, n+1), n//2)
    for p in picks:
        remains = works - set(p)
        morning = 0
        for i, j in comb(p, 2):
            morning += pij[i-1][j-1]
        night = 0
        for i, j in comb(remains, 2):
            night += pij[i-1][j-1]
        answer = min(answer, abs(morning - night)) 
    return answer

print(solution(*solution_input()))
