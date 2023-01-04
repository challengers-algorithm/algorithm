# https://school.programmers.co.kr/learn/courses/30/lessons/147354
# 예상 알고리즘: 구현
# 베스트 알고리즘: 구현

def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))

    S_i = [sum(map(lambda x: x % i, d))
           for i, d in enumerate(data[row_begin-1:row_end], row_begin)]
    answer = 0
    for i in S_i:
        answer ^= i
    return answer


print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))  # 4
