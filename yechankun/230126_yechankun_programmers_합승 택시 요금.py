# https://school.programmers.co.kr/learn/courses/30/lessons/72413
# 예상 알고리즘: 다익스트라, 플로이드 와샬
# 베스트 알고리즘: 플로이드 와샬


# 플로이드 와샬로 모든 노드간의 거리를 저장하고
# 경유지를 M이라 한다면
# S->M, M->A, M->B의 합이 최소가 되는 지점을 구한다.
def solution(n, s, a, b, fares):
    N = n+1 # n+1 기준으로 배열이 동작한다.
    answer = float('inf')
    # 가독성이 좋은 2차원 배열을 간선의 표현으로 사용
    lines = [[0 if i==j else float('inf') for j in range(N)] for i in range(N)]
    for fr, to, weight in fares:
        lines[fr][to] = weight
        lines[to][fr] = weight

    for k in range(N):
        for i in range(N):
            for j in range(N):
                lines[i][j] = min(lines[i][j], lines[i][k]+lines[k][j])
    
    for i in range(1, N):
        answer = min(answer, lines[s][i]+lines[i][a]+lines[i][b])

    return answer

print(solution(	6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
