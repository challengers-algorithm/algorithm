# https://www.acmicpc.net/problem/3197
# 예상 알고리즘: BFS
# 베스트 알고리즘: BFS

import sys
input = sys.stdin.readline

drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solutionInput():
    R, C = map(int, input().split())
    lake = []
    LPos = []
    meltQueue = []
    for r in range(R):
        lake.append(list(input().strip()))
        for c in range(C):
            if lake[r][c] != 'X':
                meltQueue.append((r, c))
            if lake[r][c] == "L":
                lake[r][c] = "."
                LPos.append((r, c))
    return R, C, lake, LPos, meltQueue

def solution(R, C, lake, LPos, meltQueue):
    moveQueue, goal = [LPos[0]], LPos[1]
    visited = [[False] * C for _ in range(R)]
    
    answer = 1
    while meltQueue:
        
        nextMeltQ, nextMoveQ = [], []
        for r, c in meltQueue:
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and lake[nr][nc] == "X":
                    lake[nr][nc] = "."
                    nextMeltQ.append((nr, nc))
        meltQueue=nextMeltQ
        for r, c in moveQueue:
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                
                if nc < 0 or nc >= C or nr < 0 or nr >= R or visited[nr][nc]:
                    continue
                visited[nr][nc] = True
                if (nr, nc) == goal:
                    return answer
                if lake[nr][nc] == ".":
                    moveQueue.append((nr, nc))
                elif lake[nr][nc] == "X":
                    nextMoveQ.append((nr, nc))
        moveQueue = nextMoveQ 
        answer += 1 
    return answer

R, C, lake, LPos, meltQueue = solutionInput()
print(solution(R, C, lake, LPos, meltQueue))
