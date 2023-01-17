# https://school.programmers.co.kr/learn/courses/30/lessons/12985
# 예상 알고리즘: 구현, 수학
# 베스트 알고리즘: 비트연산, 수학

# O(N)의 복잡도
def solution(n,a,b):
    queue:list = [False] * n
    queue[a-1], queue[b-1] = True, True
    round = 1
    while True:
        nextQueue = []
        while queue:
            a = queue.pop()
            b = queue.pop() 
            if a and b:
                return round
            nextQueue.append(a or b)
        queue = nextQueue
        round += 1

# 최선 풀이 O(1) 복잡도
# def solution(n,a,b):
    # return ((a-1)^(b-1)).bit_length()
print(solution(8, 4, 7))
print(solution(16, 9, 12))  # 2
print(solution(8, 1, 2 ))
print(solution(8, 2, 3))
print(solution(8, 4, 5))