# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 예상 알고리즘: 우선순위 큐, 그리디
# 베스트 알고리즘: 우선순위 큐, 그리디

# 대기중인 것은 작업시간순으로 정렬 필요, 작업시간과 대기시간의 총합이 더 작아야함.
# 앞서 대기중인 총 작업시간과 다음 시작시간이 겹치지 않는다면 다음 순위로 시작
from heapq import heappush, heappop
def solution(jobs):
    L = len(jobs)
    jobs.sort()
    heap = [] #뒤집어서 첫 번째 집어넣기
    # 힙이 빌 때까지 반복
    jobIdx = 0
    endTime = 0
    answer= 0 
    while jobIdx < L:
        nStart, nJobTime =  jobs[jobIdx]
        heappush(heap, [nJobTime, nStart])
        jobIdx += 1
        while heap:
            jobTime, start = heappop(heap)
            endTime = jobTime + (start if start > endTime else endTime) # 현재 일이 끝나는 시간
            answer += endTime - start
            while jobIdx < L and jobs[jobIdx][0] <= endTime:
                nStart, nJobTime =  jobs[jobIdx]
                heappush(heap, [nJobTime, nStart])
                jobIdx+=1
    return answer // len(jobs)


# print(solution(	[[0, 3], [1, 9], [2, 6]]))
# 
# print(solution(	[[7, 8], [3, 5], [9, 6]]))
# print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))
print(solution([[0,3],[4,3],[10,3]]))
# print(solution([[0,10],[2,3],[9,3]]))
# print(solution([[0,10]]))
# print(solution([[0,10], [4,10], [5,11], [15,2]]))
# print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))
# print(solution(	[[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]))


