# https://www.codetree.ai/training-field/frequent-problems/max-sum-of-tetris-block/description
# 예상 알고리즘: 구현
# 베스트 알고리즘: 구현

import sys
input = sys.stdin.readline

def solutionInput():
    n, m = map(int, input().split())
    board = [list(map(int, input().split()))]
    return n, m, board

class Tetris:
    def __init__(s): # 테트리스 블럭들
        s.blocks = [ 
                [[0, 1], [0, 2], [0, 3]], 
                [[0, 1], [1, 1], [1, 0]],
                [[1, 0], [1, 1], [2, 1]],
                [[1, 0], [2, 0], [2, 1]],
                [[1, 0], [1, 1], [2, 0]]
        ]
    
    def rotate(s): # 테트리스 블럭 회전
        for block in s.blocks:
            for i in range(3):
                block[i][0], block[i][1] = -block[i][1], block[i][0]         

def solution(n, m, board):
    t = Tetris()
    answer = 0
    for r in range(n):
        for c in range(m):
            for block in t.blocks:
                for i in range(4): # 4번 돌기
                    temp = board[r][c] # 합산 넣기
                    for dr, dc in block:
                        nr, nc = r + dr, c + dc
                        if not (0 <= nr < n and 0 <= nc < c):
                            break
                        temp += board[nr][nc]
                    else: # 전체를 제대로 돈 경우에만 최대값 갱신
                        answer = max(answer, temp)
                    t.rotate()
    return answer

print(solution(*solutionInput()))
