# https://www.codetree.ai/training-field/frequent-problems/dragon-curve
# 예상 알고리즘: 구현, 수학
# 베스트 알고리즘: 구현, 수학

import sys
input = sys.stdin.readline

def solution_input():
    n = int(input())
    dragon_curves = [list(map(int, input().split())) for _ in range(n)]
    return n, dragon_curves

def solution(n, dragon_curves):
    answer = 0
    dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    board = [[False]*100 for _ in range(100)]
    checks = set()
    for x, y, d, g in dragon_curves:
        dragon = [dxy[d]]
        visited(checks, board, x, y)
        dx, dy = dxy[d]        
        x, y = x + dx, y + dy
        visited(checks, board, x, y)

        for _ in range(g):
            for i in range(len(dragon) - 1, -1, -1):
                dx, dy = dragon[i]
                dx, dy = -dy, dx
                x, y = x + dx, y + dy
                visited(checks, board, x, y)         
                dragon.append((dx, dy))
    for x, y in checks:
        answer += check_square(x, y, board)
    return answer

def visited(checks, board, x, y):
    board[x][y] = True
    checks.add((x,y))

def check_square(x, y, board):
    dxy = [(1, 0), (0, 1), (1, 1)]
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if -1 < nx < 101 and -1 < ny < 101:
            if not board[nx][ny]:
                return False
    return True

print(solution(*(solution_input())))