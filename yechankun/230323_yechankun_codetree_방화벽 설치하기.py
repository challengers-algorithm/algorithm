# https://www.codetree.ai/training-field/frequent-problems/firewall-installation
# 예상 알고리즘: BFS
# 베스트 알고리즘: BFS, 백트래킹
import sys
input = sys.stdin.readline

def solutionInput():
    n, m = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(n)]
    fires = []
    blanks = []
    for r in range(n):
        for c in range(m):
            if ground[r][c] == 2:
                fires.append((r,c))
            elif ground[r][c] == 0:
                blanks.append((r,c))

    return n, m, ground, fires, blanks

from itertools import combinations

def solution(n, m, ground, fires, blanks):
    answer = 0
    blankCnt = len(blanks) -3
    for com in combinations(blanks, 3):
        tempGround = [ground[r][:] for r in range(n)] # 깊은 복사
        for r, c in com:
            tempGround[r][c] = 1
        answer = max(answer, bfs(n, m, tempGround, fires, blankCnt))
    return answer

def bfs(n, m, ground, fires, blankCnt):
    answer = 0
    drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while fires:
        nextFires= []
        for r, c in fires:
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < m and ground[nr][nc] == 0):
                    continue
                ground[nr][nc] = 2
                nextFires.append((nr, nc))
                blankCnt -= 1
        fires = nextFires
    return blankCnt 

print(solution(*solutionInput()))