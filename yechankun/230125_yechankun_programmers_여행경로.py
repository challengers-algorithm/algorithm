# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 예상 알고리즘: DFS
# 베스트 알고리즘: DFS

from collections import defaultdict

# 방문 순서를 저장해야 한다는 점에서 DFS가 유리함.
# 미리 방문지점의 알파벳을 정렬해야 함.
def solution(tickets):
    answer = []
    directDict = defaultdict(list)
    for fr, to in tickets:
        directDict[fr].append(to)
    for d in directDict:
        directDict[d].sort()
    visited = defaultdict(int)
    for fr in directDict:
        for to in directDict[fr]:
            visited[(fr, to)] += 1
    answer, _ = dfs("ICN", 0, len(tickets), directDict, visited)

    return answer

def dfs(curr, currCnt, totalCnt, directDict, visited):
    answer = [curr]
    for to in directDict[curr]:
        if visited[(curr, to)] == 0:
            continue
        visited[(curr, to)] -= 1
        tempCtn = currCnt
        dfsAnswer, currCnt = dfs(to, currCnt+1, totalCnt, directDict, visited)
        if currCnt != totalCnt:
            visited[(curr, to)] += 1
            currCnt = tempCtn
            continue            
        answer += dfsAnswer
        break
    return answer, currCnt




print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# ["ICN", "JFK", "HND", "IAD"]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

print(solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]))
# ["ICN", "CCC", "DDD", "ICN", "AAA", "BBB", "AAA", "BBB"]