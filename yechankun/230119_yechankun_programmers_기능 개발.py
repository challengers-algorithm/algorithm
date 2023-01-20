# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 예상 알고리즘: 그리디
# 베스트 알고리즘: 큐

def solution(progresses, speeds):
    ps = list(zip(progresses, speeds))
    answer = []
    while ps:
        temp = []
        a = 0
        for p, s in ps:
            if p+s >= 100 and not temp:
                a += 1
                continue
            temp.append((p+s, s))
        if a > 0:
            answer.append(a)
        ps = temp
    return answer


print(solution(	[93, 30, 55], [1, 30, 5]))
