# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 예상 알고리즘: 해시
# 베스트 알고리즘:

from heapq import heappush, heappop
def solution(genres, plays):
    answer = []
    playsGenresDict = {x:[] for x in genres}
    totalPlaysGenres = {x:0 for x in genres}
    for i in range(len(genres)-1, -1, -1):
        genre, play = genres[i], plays[i]
        heappush(playsGenresDict[genre], (-play, i))
        totalPlaysGenres[genre] += play

    sortedPlaysGenres = sorted(totalPlaysGenres.items(), key=lambda x: -x[1])
    for genre, _ in sortedPlaysGenres:
        for i in range(2):
            if not playsGenresDict[genre]:
                break
            answer.append(heappop(playsGenresDict[genre])[1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop", "asdf"], [500, 500, 150, 500, 2500, 1]))