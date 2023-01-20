# https://school.programmers.co.kr/learn/courses/30/lessons/64062
# 예상 알고리즘: 슬라이딩 윈도우, 최대 힙
# 베스트 알고리즘: 

from heapq import heappush, heappop
from collections import defaultdict
def solution(stones, k):
    answer = 1
    L = len(stones)
    maxHeap = []
    answer = float('inf')
    right = k 
    lastIdx = 0
    temp = defaultdict(int)    
    for left in range(L-k+1):
        for i in range(lastIdx, right):
            heappush(maxHeap, (-stones[i], i))
        while maxHeap[0][1] < left:
            heappop(maxHeap)
        answer = min(answer, -maxHeap[0][0])     
        lastIdx = right
        right = right + 1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))