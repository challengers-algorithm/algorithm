# https://school.programmers.co.kr/learn/courses/30/lessons/67259
# 예상 알고리즘: BFS, DFS, 백트래킹
# 베스트 알고리즘: BFS, DP

from collections import defaultdict
drc=((1, 0), (0, -1), (-1, 0), (0, 1)) # 하 좌 상 우
dDrc = ((-1, 600), (0, 100), (1, 600))
def solution(board):
    L = len(board)
    queue = [(0,0,0,0), (0,0,3,0)] #r, c, direct, cost
    costs = defaultdict(int)
    costs[(0,0,0)] = costs[(0,0,3)] = 0
    while queue:
        nextQueue = []
        for r, c, dir, cost in queue:
            for d, plus in dDrc:
                nd = (dir + d)%4
                dr, dc = drc[nd]
                nr = r + dr
                nc = c + dc
                if 0 <= nr < L and 0 <= nc < L and not board[nr][nc]:
                    nCost = cost + plus
                    if (nr,nc,nd) not in costs or costs[(nr,nc,nd)] > nCost:
                        nextQueue.append((nr,nc, nd, nCost))
                        costs[(nr,nc,nd)] = nCost      
        queue = nextQueue
    return min([costs.get((L-1,L-1, i), float('inf')) for i in range(4)])


# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# 900

# print(solution(	[[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
# # 3800

# print(solution(	[[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))

# print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))
# # 3200

print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))