# 
# 예상 알고리즘: 그리디, 구현, 우선순위 큐
# 베스트 알고리즘:

# 우선순위 큐로 풀 수 있을 듯 하다.

from heapq import heappush, heappop
def solution(k, score):
    answer = []
    queue = []
    for s in score:
        if len(queue) == k:
            if queue[0] < s:
                heappop(queue)
                heappush(queue, s)
        else:
            heappush(queue, s)
        answer.append(queue[0])
    return answer

print(solution(	3, [10, 100, 20, 150, 1, 100, 200]))