# https://school.programmers.co.kr/learn/courses/30/lessons/131130
# 예상 알고리즘: 해싱
# 베스트 알고리즘: 정렬

def solution(cards):
    answer = 0
    cardSet = set(cards)
    cards = [0] + cards
    cardPos = [0] * len(cards)
    for i in range(1, len(cards)):
        cardPos[cards[i]] = i
    setList1 = []

    # 1차 그룹
    for idx, card in enumerate(cards):
        visited = [False] * (len(cards))
        group = set([idx])
        now = card
        while visited[now] == False:
            visited[now] = True
            group.add(now)
            now = cards[now]
        setList1.append(group)
    # 2차 그룹
    for idx, card in enumerate(cardSet, 1):
        leftCardSet = cardSet-setList1[idx]
        for i, c in enumerate(leftCardSet, 1):
            group = [cardPos[c]]
            setList2 = set(setList1[idx])
            setList2.add(cardPos[c])
            now = c
            while now not in setList2:
                setList2.add(now)
                group.append(now)
                now = cards[now]
            answer = max(answer, len(setList1[idx])*len(group))
    return answer

print(solution([8, 6, 3, 7, 2, 5, 1, 4]))
