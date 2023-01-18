# https://school.programmers.co.kr/learn/courses/30/lessons/12980
# 예상 알고리즘: 수학
# 베스트 알고리즘: 수학

# 남은 거리를 반으로 나누면서 2로 나눈 나머지 더하기
def solution(n):
    ans = 0
    while n >= 1:
        remain = n % 2
        ans += remain
        n//=2

    return ans

print(solution(5)) #2

print(solution(6)) #2

print(solution(5000)) #5