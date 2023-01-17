# https://school.programmers.co.kr/learn/courses/30/lessons/12949
# 예상 알고리즘: 구현, 수학
# 베스트 알고리즘: 수학적인 무언가

def solution(arr1, arr2):
    R = len(arr1)
    cR = len(arr1[0])
    C = len(arr2[0])
    answer = [[0] * C for _ in range(R)]
    for i in answer:
        print(i)
    for r in range(R):
        for c in range(C):
            for cr in range(cR):
                answer[r][c] += arr1[r][cr] * arr2[cr][c]    
    
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))