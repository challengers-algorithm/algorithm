# https://school.programmers.co.kr/learn/courses/30/lessons/136798
# 예상 알고리즘: 수학, 에라스토테네스의 체
# 베스트 알고리즘: 수학


def solution(number, limit, power):
    answer = 0
    dp = calculateAllWeaponDMG(number)
    for i in range(1, number+1):
        dmg = len(dp[i])
        if dmg > limit:
            answer += power
            continue
        answer += dmg
    return answer

def calculateAllWeaponDMG(num):
    dp = {i: set([1, i]) for i in range(1, num+1)}
    for i in range(2, int(num**0.5)+1):
        for j in range(1, (num)//i+1):
            dp[i*j].update((i, j))
    return dp

# print(solution(5, 3, 2))
print(solution(10, 3, 2))