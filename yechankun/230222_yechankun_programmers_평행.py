# https://school.programmers.co.kr/learn/courses/30/lessons/120875
# 예상 알고리즘: 조합

from itertools import combinations

def solution(dots):
    idxs = {0,1,2,3}
    for line1 in combinations(idxs, 2):
        line2 = list(idxs - set(line1))
        if getGrad(dots[line1[0]], dots[line1[1]]) == getGrad(dots[line2[0]], dots[line2[1]]):
            return 1
    return 0

def getGrad(dot1, dot2):
    return (dot2[1]-dot1[1]) / (dot2[0]-dot1[0])


print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))