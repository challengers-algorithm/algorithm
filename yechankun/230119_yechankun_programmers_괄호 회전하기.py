# https://school.programmers.co.kr/learn/courses/30/lessons/76502
# 예상 알고리즘: 스택, 큐
# 베스트 알고리즘: 스택, 큐

from collections import deque

bracketDict = {')':'(', ']':'[', '}':'{'}

def isCorrect(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if stack and bracketDict.get(s[i], 'x') == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    return len(stack) == 0

def solution(s):
    answer = 0
    queue = deque(s)
    for _ in range(len(s)):
        answer += isCorrect(queue)
        queue.append(queue.popleft())
    return answer

print(solution('[](){}'))