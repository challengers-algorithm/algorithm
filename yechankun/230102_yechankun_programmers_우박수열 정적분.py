# https://school.programmers.co.kr/learn/courses/30/lessons/134239
# 예상 알고리즘: dp
# 베스트 알고리즘: dp

# 구간합 DP를 활용한 풀이
def solution(k, ranges):
    graph = getGraph(k)
    prefixSum = getPrefixSum(graph)
    L = len(graph)
    answer = []

    for left, right in ranges:
        if L + right <= left:
            answer.append(-1)
            continue
        answer.append(prefixSum[right - 1] - prefixSum[left])
    return answer

def getGraph(k):
    graph = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        graph.append(k)
    return graph

def getPrefixSum(graph):
    prefixSum = [0]
    for i in range(1, len(graph)):
        prefixSum.append(prefixSum[-1] + (graph[i-1]+graph[i])/2)
    return prefixSum

print(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]))