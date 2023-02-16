# https://www.acmicpc.net/problem/1427
# 베스트 알고리즘: 정렬

def solutionInput():
    N = input()
    return N

def solution(N):
    answer = ''.join(sorted(N, reverse=True))
    return answer

print(solution(solutionInput()))