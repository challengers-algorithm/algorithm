# https://www.codetree.ai/training-field/frequent-problems/virus-detector
# 예상 알고리즘: 그리디
# 베스트 알고리즘: 그리디

import sys
input = sys.stdin.readline

def solutionInput():
    n = int(input())
    cusN = list(map(int, input().split()))
    leader, emp = list(map(int, input().split()))
    return n, cusN, leader, emp

import math
def solution(n, cusN, leader, emp):
    answer = n
    for c in cusN:
        remain = c - leader
        if remain > 0:
            answer += math.ceil(remain / emp)
    return answer

print(solution(*solutionInput()))