# https://school.programmers.co.kr/learn/courses/30/lessons/12941
# 예상 알고리즘: 정렬
# 베스트 알고리즘: 정렬

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))