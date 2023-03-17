# https://www.codetree.ai/training-field/frequent-problems/cube-rounding/description
# 예상 알고리즘: 구현
# 베스트 알고리즘: 구현

import sys
input = sys.stdin.readline

def solutionInput():
    n, m, x, y, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ops = list(map(int,input().split()))
    return n,m,x,y,k, board, ops

class Dice:
    # 5면체를 2차원배열로 만들고  1면(top)은 변수로 두기
    # 바닥은 1, 1 좌표
    def __init__(s, num):
        s.dices = [[0]*3 for _ in range(3)]
        s.top = 0
        s.dices[1][1] = num
    def rolling(s, op, num):
        if op == 1:
            s.top, temp = s.dices[1][0], s.top
            for i in range(2):
                s.dices[1][i] = s.dices[1][i+1]
            s.dices[1][2] = temp
        elif op == 2:
            s.top, temp = s.dices[1][2], s.top
            for i in range(2, 0, -1):
                s.dices[1][i] = s.dices[1][i-1]
            s.dices[1][0] = temp
        elif op == 3:
            s.top, temp = s.dices[2][1], s.top
            for i in range(2, 0, -1):
                s.dices[i][1] = s.dices[i-1][1]
            s.dices[0][1] = temp
        elif op == 4:
            s.top, temp = s.dices[0][1], s.top
            for i in range(2):
                s.dices[i][1] = s.dices[i+1][1]
            s.dices[2][1] = temp
        if num != 0:
            s.dices[1][1] = num 
        return s.top, s.dices[1][1]

def solution(n,m,x,y,k, board, ops):
    answer = []
    dice = Dice(board[x][y])
    board[x][y] = 0
    dxy = ((0, 0),(0, 1), (0, -1), (-1, 0), (1, 0))
    for op in ops:
        dx, dy = dxy[op]
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            x, y = nx, ny
            top, bottom = dice.rolling(op, board[x][y])
            board[x][y] = bottom if board[x][y] == 0 else 0
            answer.append(top)
    return answer

print(*solution(*solutionInput()), sep='\n')