# https://www.acmicpc.net/problem/2108
# 베스트 알고리즘: 정렬

import sys
input = sys.stdin.readline

def solutionInput():
    N = int(input())
    numbers = [int(input()) for i in range(N)]
    return N, numbers

def solution(N, numbers):
    numbers.sort()
    avg = int("%.0f" % (sum(numbers)/N))
    cent = int("%.0f" % (numbers[N//2]))
    from collections import Counter
    counter = Counter(numbers)
    counterList =  counter.most_common()
    cntFilter = [i for i, c in counterList if c == counterList[0][1]]
    cntFilter.sort()
    fre = cntFilter[0] if len(cntFilter) == 1 else cntFilter[1]
    rag = numbers[-1] - numbers[0]

    return avg, cent, fre, rag

print(*solution(*solutionInput()), sep='\n')