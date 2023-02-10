def solution(arr):
    if arr: 
        arr.remove(min(arr))
        return arr
    return [-1]

print(solution([4,3,2,1]))