# https://school.programmers.co.kr/learn/courses/30/lessons/17678
# 예상 알고리즘: 구현, 해시
# 베스트 알고리즘: 구현, 해시, 정렬, 리스트


# 시간을 분으로 나타낸 후 해싱함
def solution(n, t, m, timetable):
    start = convertTimeToMin("9:00")
    last = start + (n-1)*t
    minTable = sorted(map(convertTimeToMin, timetable), reverse=True)
    seats = {}
    for currentBus in range(start, start+t*n, t):        
        seats[currentBus] = []
    for currentBus in range(start, start+t*n, t):        
        while minTable and currentBus >= minTable[-1] and len(seats[currentBus]) < m:
            seats[currentBus].append(minTable.pop())
        
    answer = sorted(seats.keys())
    if answer and len(seats[answer[-1]]) == m:
            return convertMinToTime(seats[last][-1]-1)
    return convertMinToTime(last)
    
def convertTimeToMin(s):
    h, m = map(int, s.split(':'))
    return h*60 + m

def convertMinToTime(m):
    return '%02d:%02d'%(m//60, m%60)


# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
# print(solution(	2, 10, 2, ["09:10", "09:09", "08:00"]))
# print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
# print(solution(	1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
# print(solution(1, 1, 1, ["23:59"]))
# print(solution(	10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
# print(solution(10, 25, 1, ["09:00", "09:10" ,"09:20" ,"09:30" ,"09:40" ,"09:50",
# "10:00", "10:10" ,"10:20" ,"10:30" ,"10:40" ,"10:50"]))
# print(solution(1, 10, 3, ["08:55", "08:55", "08:59"]))
print(solution(3,1,2,["06:00", "23:59", "05:48", "00:01", "00:01"]))