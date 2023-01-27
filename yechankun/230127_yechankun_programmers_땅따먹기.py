# https://school.programmers.co.kr/learn/courses/30/lessons/12913
# 예상 알고리즘: DP
# 베스트 알고리즘: DP

def solution(land):
    for r in range(1, len(land)):
        for c in range(4):
            tempMax = 0
            for i in range(4):
                if i == c:
                    continue
                tempMax = max(tempMax, land[r-1][i])
            land[r][c] = tempMax + land[r][c]
    return max(land[-1])

print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))