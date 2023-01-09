#
# 예상 알고리즘: 문자열
# 베스트 알고리즘: 문자열

def solution(s):
    answer = 0
    temp = s[0]
    first, another = 0, 0
    for i in range(0, len(s)):
        if first == another:
            first, another = 0, 0
            answer += 1
            temp = s[i]
        if temp == s[i]:
            first += 1
        else:
            another += 1
    return answer


print(solution("banana"))
