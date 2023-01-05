# https://www.acmicpc.net/problem/1655
# 예상 알고리즘: 이진탐색
# 베스트 알고리즘:

from bisect import bisect_left
from collections import deque
import sys, math
input = sys.stdin.readline

def solutionInput():
    N = int(input())
    numbers = [int(input()) for _ in range(N)]
    return N, numbers

# 정렬을 이용하게 되면 N^2가 되어 10만*10만=100억의 계산이 필요하다
# 이진탐색을 이용해 삽입 위치를 판단하는 방법이 있다. (logN)*N 이진 이 된다.
# 대충 16*10만= 160만번 반복하면 되므로 효율적이다.
def solution(N, numbers):
    speakNumbers = deque()
    answer = []
    for number in numbers:
        nextInsertIdx = bisect_left(speakNumbers, number)
        speakNumbers.insert(nextInsertIdx, number)
        answer.append(speakNumbers[math.ceil(len(speakNumbers)/2)-1])
    return answer

print(*solution(*solutionInput()), sep='\n')
