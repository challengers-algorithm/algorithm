# https://school.programmers.co.kr/learn/courses/30/lessons/133500
# 예상 알고리즘: 트리
# 베스트 알고리즘: 트리, DFS

from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**9)

def solution(n, lighthouse):
    answer = 0
    # 트리구조
    graph = getGraph(lighthouse)
    tree = getTree(n, 1, graph)

    def dfs(start, tree):
        nonlocal answer
        if not start in tree:
            return False
        isLightOn = True

        for i in tree[start]:
            isLightOn &= dfs(i, tree)
        isLightOn = not isLightOn

        if isLightOn:
            answer += 1
        return isLightOn

    dfs(1, tree)
    return answer

def getGraph(lighthouse):
    graph = defaultdict(set)
    for start, to in lighthouse:
        graph[start].add(to)
        graph[to].add(start)
    return graph

def getTree(n, start, graph):
    queue = deque([start])
    tree = defaultdict(set)
    visited = [False] * (n+1)
    while queue:
    # tree 추가
        now = queue.popleft()
        if visited[now]:
            continue
        visited[now] = True
        for next in graph[now]:
            if not visited[next]:
                tree[now].add(next)
                queue.append(next)
    return tree