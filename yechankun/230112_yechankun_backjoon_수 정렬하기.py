# https://www.acmicpc.net/problem/2750
# 예상 알고리즘: 퀵 정렬
# 베스트 알고리즘: 퀵 정렬, 해시 정렬

import sys
sys.setrecursionlimit(10**7)

def solutionInput():
    N = int(input())
    numbers = [int(input()) for _ in range(N)]
    return N, numbers

# 퀵 정렬
def solution(N, numbers):
    answer = quickSort(numbers, 0, N-1)
    return answer

def quickSort(numbers, start, end):    
    stack = [(start, end)]

    while stack:
        start, end = stack.pop()
        if start >= end: 
            continue
        left = start+1
        right = end
        while left <= right:
            while left <= end and numbers[start] >= numbers[left]:
                left += 1
            while right > start and numbers[start] <= numbers[right]:
                right -= 1
            if left > right:
                numbers[start], numbers[right] = numbers[right], numbers[start]
            else:
                numbers[right], numbers[left] = numbers[left], numbers[right]
        stack.append((start, right - 1))
        stack.append((right + 1, end))
    return numbers

print(*solution(*solutionInput()), sep='\n')