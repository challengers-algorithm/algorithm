# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 예상 알고리즘: DP
# 베스트 알고리즘: DP

def solution(m, n, puddles):
    board = [[0]*(m+1) for _ in range(n+1)]
    puddles = set(map(tuple, puddles))
    for r in range(1, n+1):
        for c in range(1, m+1):
            if (c, r) in puddles:
                continue
            board[r][c] = (board[r][c-1] + board[r-1][c]) %  1000000007
            board[1][1] = 1
    return board[n][m]

print(solution(4, 3, [[2, 1]])) #4