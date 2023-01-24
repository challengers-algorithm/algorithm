# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 예상 알고리즘: 크루스칼
# 베스트 알고리즘


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    pathDict = {x: x for x in range(n)}
    for s, t, cost in costs:
        if find(pathDict, s) != find(pathDict, t):
            union(pathDict, s, t)
            answer += cost    
    return answer

print(solution(	4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])) # 4