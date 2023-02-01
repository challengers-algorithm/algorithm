# https://school.programmers.co.kr/learn/courses/30/lessons/49191
# 예상 알고리즘: 그래프, BFS, 플로이드 워셜
# 베스트 알고리즘: 그래프 순회

from collections import defaultdict
def solution(n, results):
    answer = 0

    winDict = defaultdict(set)
    loseDict = defaultdict(set)

    for w, l in results:
        winDict[w].add(l)
        loseDict[l].add(w)

    resultWinsDict = defaultdict(set)
    resultLoseDict = defaultdict(set)

    for i in range(1, n+1):
        bfs(i, resultWinsDict, winDict)
        bfs(i, resultLoseDict, loseDict)
    
    for i in resultWinsDict:
        if len(resultWinsDict[i]) + len(resultLoseDict[i]) == n-1:
            answer += 1
    return answer

def bfs(start, resultDict, searchDict):
    queue = [start]
    visited = set([start])
    while queue:
        nextQueue = []
        for node in queue:
            for i in searchDict[node]:
                if i in visited:
                    continue
                visited.add(i)
                resultDict[i].add(node)
                for j in resultDict[node]:
                    resultDict[i].add(j)
                nextQueue.append(i)
        queue = nextQueue


print(solution(	5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))