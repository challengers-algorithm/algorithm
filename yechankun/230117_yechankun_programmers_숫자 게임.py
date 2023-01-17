# https://school.programmers.co.kr/learn/courses/30/lessons/12987
# 예상 알고리즘: 그리디
# 베스트 알고리즘: 그리디

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    N = len(A)
    aIdx, bIdx = 0, 0
    while aIdx < N and bIdx < N:
        if A[aIdx] < B[bIdx]:
            answer += 1
            bIdx += 1
        else:
            aIdx -= 1
            bIdx += 1
        aIdx += 1
    return answer

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))

print(solution([2, 2, 2, 2], [1, 1, 1, 1]))

print(solution([1,2,3,4,5,6], [1,2,3,4,5,6]))