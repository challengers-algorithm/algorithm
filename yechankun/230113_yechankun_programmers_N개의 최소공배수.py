# https://school.programmers.co.kr/learn/courses/30/lessons/12953
# 예상 알고리즘: 수학
# 베스트 알고리즘: 수학

def solution(arr):
    dp = {x: 0 for x in range(2, 101)}

    for a in arr:
        curr = 2
        cnt = 0
        while a != 1:
            if a % curr == 0:
                a //= curr
                cnt += 1
            else:
                dp[curr] = max(cnt, dp[curr])
                curr += 1
                cnt = 0
        else:
            dp[curr] = max(cnt, dp[curr])
    answer = 1
    for i in dp:
        answer *= i**dp[i]
    return answer

print(solution([3, 6, 8, 14]))
print(solution([14, 2, 7]))