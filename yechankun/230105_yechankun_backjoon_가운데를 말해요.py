# https://www.acmicpc.net/problem/1655
# 예상 알고리즘: 이진탐색
# 베스트 알고리즘: 우선순위 큐

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def solutionInput():
    N = int(input())
    numbers = [int(input()) for _ in range(N)]
    return N, numbers

# 파이썬의 deque의 insert 시간복잡도는 O(n)이므로 bisect_left를 쓰는 것은 잘못됐다.
# LinkedList는 bisect_left를 쓸 수 없으므로 이를 통해 풀이할 수 없다.
# 대신 우선순위 큐를 사용한다.
def solution(N, numbers):
    maxHeap = []
    minHeap = []
    answer = []
    for idx, number in enumerate(numbers):
        if idx % 2 == 0:
            heappush(maxHeap, -number)
        else:
            heappush(minHeap, number)
        if minHeap and maxHeap and -maxHeap[0] > minHeap[0]:
            maxNum = -heappop(maxHeap)
            minNum = heappop(minHeap)
            heappush(maxHeap, -minNum)
            heappush(minHeap, maxNum)
        answer.append(-maxHeap[0])
    return answer

print(*solution(*solutionInput()), sep='\n')
