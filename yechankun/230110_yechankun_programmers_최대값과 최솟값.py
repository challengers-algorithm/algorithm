# https://school.programmers.co.kr/learn/courses/30/lessons/12939
# 예상 알고리즘: 문자열, 정렬
# 베스트 알고리즘: 문자열, 정렬

def solution(s):
    nums = sorted(map(int, s.split()))
    return str(nums[0]) + ' ' + str(nums[-1])


print(solution(	"1 2 3 4"))