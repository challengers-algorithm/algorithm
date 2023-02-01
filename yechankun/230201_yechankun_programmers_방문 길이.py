# https://school.programmers.co.kr/learn/courses/30/lessons/49994
# 예상 알고리즘: 방향 벡터
# 베스트 알고리즘: 방향 벡터

def solution(dirs):
    drc = {'U':(1, 0), 'D':(-1, 0), 'R':(0, 1), 'L':(0,-1)}
    visited = set()
    r, c = 0, 0
    for op in dirs:
        dr, dc = drc[op]
        nr = r + dr
        nc = c + dc
        if -5 <= nr <= 5 and -5 <= nc <= 5:
            visited.update([(nr, nc, r, c), (r, c, nr, nc)])
            r, c = nr, nc
    return len(visited) // 2


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))