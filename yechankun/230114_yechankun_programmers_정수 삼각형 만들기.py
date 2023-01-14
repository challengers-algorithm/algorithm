# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 베스트 알고리즘: DP

def solution(triangle):
    cTriangle = [[0] + x + [0] for x in triangle]
    for i in range(1, len(cTriangle)):
        for j in range(1, len(cTriangle[i])-1):
            left, right = cTriangle[i-1][j-1], cTriangle[i-1][j]
            cTriangle[i][j] = max(cTriangle[i][j]+left, cTriangle[i][j]+right)
    return max(cTriangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) # 30
