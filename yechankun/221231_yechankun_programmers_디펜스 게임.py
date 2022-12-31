# https://school.programmers.co.kr/learn/courses/30/lessons/142085
# 예상 알고리즘: 우선순위큐
# 베스트 알고리즘: 우선순위큐

from heapq import heappush, heappop

def solution(n, k, enemy):
    heap = []
    for round, e in enumerate(enemy):
        heappush(heap, e)
        if len(heap) > k:
            n -= heappop(heap)
        
        if n < 0 :
            return round
    return len(enemy)

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))