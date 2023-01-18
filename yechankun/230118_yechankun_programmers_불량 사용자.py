# https://school.programmers.co.kr/learn/courses/30/lessons/64064
# 예상 알고리즘: 순열, DFS
# 베스트 알고리즘: 순열, DFS

def solution(user_id, banned_id):
    answer = []
    userL, banL = len(user_id), len(banned_id) 
    userPerList = permutation(user_id, banL, [False]*userL)
    for userList in userPerList:
        for user, banned  in zip(userList, banned_id):
            if isInclude(user, banned):
                continue
            break
        else:
            if set(userList) not in answer:
                answer.append(set(userList))
    return len(answer)

def permutation(arr, n, selected):
    result = []
    if n == 0:
        return [[]]
    for i, item in enumerate(arr):
        if selected[i]:
            continue
        selected[i] = True
        for partList in permutation(arr, n-1, selected):
            result += [[item]+partList]
        selected[i] = False
    return result

def isInclude(word1, word2):
    if len(word1) != len(word2):
        return False
    for c1, c2 in zip(word1, word2):
        if c2 == "*":
            continue
        if c1 != c2:
            return False
    return True

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
