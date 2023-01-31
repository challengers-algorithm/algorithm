# https://school.programmers.co.kr/learn/courses/30/lessons/12904
# 예상 알고리즘: 구현, 슬라이딩 윈도우
# 베스트 알고리즘: DP

def solution(s):
    answer = 1
    L = len(s)
    dp = list(s)
    sReverse = s[::-1]
    dpReverse = list(s)
    for i in range(L):
        for p in range(1, L):
            if i+p >= L:
                break
            dp[i] += s[i+p]
            dpReverse[i] = sReverse[L-i-p-1] + dpReverse[i]
            if dp[i] == dpReverse[i]:
                answer = max(answer, len(dp[i]))
    return answer


print(solution("abcdcba"))
# 7

print(solution("abacde"))
# 3