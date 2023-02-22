# https://school.programmers.co.kr/learn/courses/30/lessons/120956
# 예상 알고리즘: 문자열
# 베스트 알고리즘: 문자열

def solution(babbling):
    canVoice = ["aya", "ye", "woo", "ma"]
    watchList = []
    for bb in babbling:
        for c in canVoice:
            if c * 2 in bb:
                break
        else:
            watchList.append(bb)
    answer = 0
    for i in range(len(watchList)):
        for c in canVoice:
            watchList[i] = watchList[i].replace(c, "*")   
        if watchList[i] == '*' * len(watchList[i]):
            answer += 1
    return answer