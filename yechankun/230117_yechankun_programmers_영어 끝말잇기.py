# https://school.programmers.co.kr/learn/courses/30/lessons/12981
# 예상 알고리즘: 해시
# 베스트 알고리즘: 해시

def solution(n, words):   
    wordSet = set([words[0]])
    startChar = words[0][-1]
    for i in range(1, len(words)):
        if startChar != words[i][0]:
            return [i%n+1, i//n+1]
        if words[i] in wordSet:
            return [i%n+1, i//n+1]
        wordSet.add(words[i])
        startChar = words[i][-1]
    return [0, 0]


# 3 3
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

# 0 0
print(solution(	5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))

# 1 3
print(solution(	2, ["hello", "one", "even", "never", "now", "world", "draw"]))
