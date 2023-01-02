# https://www.acmicpc.net/problem/1707
# 예상 알고리즘: BFS
# 베스트 알고리즘: BFS, DFS

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

from collections import defaultdict

def solutionInput():
    testCases = []
    for _ in range(int(input())):
        v, e = map(int, input().split())
        graph = defaultdict(list)
        for _ in range(e):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        testCases.append((v, graph))
    return testCases

def solution(testCases):
    for v, graph in testCases:
        print('YES' if isBipartiteGraph(v, graph) else 'NO')

def isBipartiteGraph(v, graph):
    colors = [0] * (v + 1)
    for i in range(1, v + 1):
        if colors[i] == 0 and not bfs(i, graph, colors):
            return False
    return True

def bfs(start, graph, colors):
    queue = [start]
    colors[start] = 1
    while queue:
        node = queue.pop(0)
        for nextNode in graph[node]:
            if colors[nextNode] == 0:
                colors[nextNode] = -colors[node]
                queue.append(nextNode)
            elif colors[nextNode] == colors[node]:
                return False
    return True

solution(solutionInput())

