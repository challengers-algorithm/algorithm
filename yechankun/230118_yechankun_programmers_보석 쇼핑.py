# https://school.programmers.co.kr/learn/courses/30/lessons/67258
# 예상 알고리즘: DP, 슬라이딩 윈도우
# 베스트 알고리즘: 슬라이딩 윈도우

from collections import defaultdict

def solution(gems):
    kinds = set(gems)
    currentKinds = defaultdict(int)
    currentSet = set()
    L = len(gems)
    mRight, mLeft = L-1, 0
    lastIdx = 0

    for left in range(L):
        # 첫번째 슬라이딩 윈도우 찾기
        for right in range(lastIdx, L):
            currentSet.add(gems[right])
            currentKinds[gems[right]] += 1
            if len(currentSet) == len(kinds):
                if mRight - mLeft > right - left:
                    mRight, mLeft = right, left
                lastIdx = max(left+1, right)
                break
        else:
            break
        currentKinds[gems[left]] -= 1
        if currentKinds[gems[left]] == 0:
            currentSet.remove(gems[left])
        currentKinds[gems[right]] -= 1
    return [mLeft+1, mRight+1]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))