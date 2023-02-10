# https://school.programmers.co.kr/learn/courses/30/lessons/12948
# 베스트 알고리즘: 슬라이싱

def solution(phone_number):
    return "*"*(len(phone_number)-4)+phone_number[-4:]