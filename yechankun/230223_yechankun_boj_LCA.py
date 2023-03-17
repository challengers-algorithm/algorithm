# https://www.acmicpc.net/problem/11437
# 예상 알고리즘: BFS, 트리
# 베스트 알고리즘: DFS, 세그먼트 트리

import sys 
input = sys.stdin.readline
sys.setrecursionlimit(100000) # 런타임 오류를 피하기 위한 재귀 깊이 제한 설정

from collections import defaultdict
def solutionInput():
    N = int(input())
    tree = defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    M = int(input())
    mInputs = []
    for _ in range(M):
        mInputs.append(list(map(int, input().split())))
    return N, tree, M, mInputs

def solution(N, tree, M, mInputs):
    FLOOR = 21 # 대략 100만개가 쭉 일렬로 그래프를 이루더라도 작동이 가능한 층수
    parents = [[0] * FLOOR for _ in range(N + 1)] # 부모 노드 정보
    depth = [0] * (N + 1) # 각 노드까지의 깊이
    visited = [0] * (N + 1) # 각 노드의 깊이가 계산되었는지 여부
    depth[0] = -1
    # 루트부터 깊이(depth)를 구하는 함수
    def getDepth(i, d):
        visited[i] = True
        depth[i] = d
        for y in tree[i]:
            if visited[y]: # 이미 깊이를 구했다면 넘기기
                continue
            parents[y][0] = i
            getDepth(y, d + 1)

    getDepth(1, 0) # 1번 노드
    for j in range(1, FLOOR):
        for i in range(1, N + 1):
            parents[i][j] = parents[parents[i][j - 1]][j - 1]
    # 최소 공통 조상을 찾는 함수
    def getLCA(a, b):
        # b가 더 깊도록 설정
        if depth[a] > depth[b]:
            a, b = b, a
        # 먼저 깊이(depth)가 동일하도록
        for i in range(FLOOR - 1, -1, -1):
            if depth[a] <= depth[parents[b][i]]:
                b = parents[b][i]
        # 깊이를 같게 맞췄더니 a와 b가 같은 경우
        if a == b:
            return a
        # 조상 탐색
        for i in range(FLOOR - 1, -1, -1):
            if parents[a][i] != parents[b][i]:
                a = parents[a][i]
                b = parents[b][i]
        return parents[a][0]

    answer = []
    for m in mInputs:
        answer.append(getLCA(*m))
    return answer

print(*solution(*solutionInput()), sep='\n')