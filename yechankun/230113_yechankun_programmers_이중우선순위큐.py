# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 예상 알고리즘: 우선순위 큐, 정렬
# 베스트 알고리즘: 우선순위 큐

from heapq import heappush, heappop
def solution(operations):
    maxQueue = []
    minQueue = []

    for ops in operations:
        if ops.startswith("I"):
            number = int(ops.split()[1])
            heappush(maxQueue, -number)
            heappush(minQueue, number)
        elif ops == "D 1":
            if maxQueue:
                minQueue.remove(-heappop(maxQueue))
        else:
            if minQueue:
                maxQueue.remove(-heappop(minQueue))
    return [-maxQueue[0], minQueue[0]] if maxQueue and minQueue else [0, 0]

print(solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))