# https://school.programmers.co.kr/learn/courses/30/lessons/42884
# 예상 알고리즘: 그리디
# 베스트 알고리즘: 그리디

def solution(routes):
    routes = list(map(sorted, routes))
    routes.sort(key=lambda x: (x[0], x[1]))
    answer = 1
    _, right = routes[0]
    print(routes)

    for i in range(1, len(routes)):
        fr, to = routes[i]

        if right >= fr:
            # left = fr
            right = min(right, to)
            continue
        else:
            answer += 1
            _, right = routes[i]
    return answer


# print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]])) #2

# print(solution([[-2,-1], [1,2],[-3,0]])) #2
# print(solution([[0,0],])) #1
# print(solution([[0,1], [0,1], [1,2]])) #1
# print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
# print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
# print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2