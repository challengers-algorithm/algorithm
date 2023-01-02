# https://school.programmers.co.kr/learn/courses/30/lessons/132266
# 예상 알고리즘: Dijkstra
# 베스트 알고리즘: Dijkstra

from collections import defaultdict
from heapq import heappush, heappop

# 다익스트라 알고리즘으로 푼다
def solution(n, roads, sources, destination):
    graphDict = getGraphDict(roads)
    dp = getDijkstra(n, graphDict, destination)
    answer = [-1 if dp[s] == float('inf') else dp[s] for s in sources]
    return answer

def getGraphDict(roads):
    graphDict = defaultdict(list)
    for a, b in roads:
        graphDict[a].append(b)
        graphDict[b].append(a)
    return graphDict

def getDijkstra(n, graphDict, destination):
    dp = [float('inf')] * (n + 1)
    dp[destination] = 0
    heap = [(0, destination)]
    while heap:
        cost, node = heappop(heap)
        for nextNode in graphDict[node]:
            if dp[nextNode] > cost + 1:
                dp[nextNode] = cost + 1
                heappush(heap, (cost + 1, nextNode))
    return dp

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))
print(solution(7, [[1, 2], [1, 4], [2, 3], [2, 4], [2, 5], [4, 5], [4, 6]], [1, 2, 3, 5, 6, 7], 5))
