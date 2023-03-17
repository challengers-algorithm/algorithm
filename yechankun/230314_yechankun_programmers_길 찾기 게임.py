# https://school.programmers.co.kr/learn/courses/30/lessons/42892
# 예상 알고리즘: 트리
# 베스트 알고리즘: 트리

import sys
sys.setrecursionlimit(10**8)

class BinaryTree:
    def __init__(s):
        s.nodes = Node()
    
    def add(s, node):
        if s.nodes.item == None:
            s.nodes.item = node
        else:
            nNum, nPos = node
            curr = s.nodes
            isLeft = False
            while curr != None:
                cNum, cPos = curr.item
                parent, isLeft = curr, False
                if cPos[0] > nPos[0]:
                    curr = curr.left
                    isLeft = True
                if cPos[0] < nPos[0]:
                    curr = curr.right
            if isLeft:
                parent.left = Node(node)
            else:
                parent.right = Node(node)
            
class Node:
    def __init__(s, item=None):
        s.left = None
        s.right = None
        s.item = item

def solution(nodeinfo):
    # 첫 번째 접근법. 높은 y의 값을 가지고 있는 것이 상위 레벨이다.
    # y 좌표 순서로 정렬한다
    node = sorted(enumerate(nodeinfo, 1), key=lambda x: (-x[1][1], x[1][0]))
    tree = BinaryTree()
    for n in node:
        tree.add(n)
    return [preOrderSearch(tree, tree.nodes), postOrderSearch(tree, tree.nodes)]

# 전위 순회
def preOrderSearch(tree, curr:Node):
    answer = [curr.item[0]]
    if curr.left != None:
        answer += preOrderSearch(tree, curr.left)
    if curr.right != None:
        answer += preOrderSearch(tree, curr.right)    
    return answer

# 후위 순회
def postOrderSearch(tree, curr:Node):
    answer = []
    if curr.left != None:
        answer += postOrderSearch(tree, curr.left)
    if curr.right != None:
        answer += postOrderSearch(tree, curr.right)
    return answer + [curr.item[0]]


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
# [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]