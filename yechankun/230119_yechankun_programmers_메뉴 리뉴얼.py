# https://school.programmers.co.kr/learn/courses/30/lessons/72411
# 예상 알고리즘: 조합, 해시
# 베스트 알고리즘: 조합, 해시

from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:        
        menus = []
        for order in orders:
            if len(order) < c:
                continue
            courseMenuList = list(combinations(order, c))
            menus.extend(map(lambda x: tuple(sorted(x)), courseMenuList))
        counter = Counter(menus).most_common()
        for menu, i in counter:
            if i == counter[0][1] and i >= 2:
                answer.append(''.join(sorted(menu)))
            else:
                break
    return sorted(answer)

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(	["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))