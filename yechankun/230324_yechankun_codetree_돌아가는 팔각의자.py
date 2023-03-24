# https://www.codetree.ai/training-field/frequent-problems/rounding-eight-angle
# 예상 알고리즘: 구현
# 베스트 알고리즘: 구현

import sys
input = sys.stdin.readline

def solution_input():
    chairs = [[0]]+[list(map(int, list(input().strip()))) for _ in range(4)]
    rotate_cnt = int(input())
    rotate_ops = [list(map(int, input().split())) for _ in range(rotate_cnt)]
    return chairs, rotate_ops

# deque를 이용해서 회전시킨다.
from collections import deque

def solution(chairs, rotate_ops):
    deq_chairs = [deque(chair) for chair in chairs]

    checks = {1: (2, 6), -1: (6, 2)}
    for n, direct in rotate_ops:
        # 큐를 이용해 푼다. 처음 들어가는 것은 양쪽을 체크해야 한다.
        queue = [([-1, 1], n, direct)]
        while queue:
            next_queue = []
            # dns는 처음 만 -1, 1이고 그 다음부터는 한쪽 방향만 포함한다.
            for dns, qn, qd in queue:
                for dn in dns: # queue수에 따라 2, 1, 1,...번씩 순회한다.
                    origin, effect = checks[dn]
                    next_qn = qn + dn
                    if 1 <= next_qn <= 4:
                        if deq_chairs[qn][origin] != deq_chairs[next_qn][effect]:
                            next_queue.append(([dn], next_qn, -qd))
                rotate(deq_chairs[qn], qd)
            queue = next_queue
    return sum([deq_chairs[i][0] * 2**(i-1) for i in range(1, 5)])

def rotate(chair: deque, direct):
    chair.rotate(direct)      

print(solution(*solution_input()))
