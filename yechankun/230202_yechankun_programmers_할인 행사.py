# https://school.programmers.co.kr/learn/courses/30/lessons/131127
# 예상 알고리즘: 슬라이딩 윈도우
# 베스트 알고리즘: 슬라이딩 윈도우

from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    wantDict = defaultdict(int)
    for w, n in zip(want, number):
        wantDict[w] = n
    currDict = defaultdict(int)

    for i in range(10):
        currDict[discount[i]] += 1
    right = 9
    L = len(discount)
    for left in range(L):
        if wantDict == currDict:
            answer += 1
        currDict[discount[left]] -= 1
        if currDict[discount[left]] == 0:
            del currDict[discount[left]]
        right += 1
        if right < L:
            currDict[discount[right]] += 1
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
