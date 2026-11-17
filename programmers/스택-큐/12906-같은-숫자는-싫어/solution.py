from collections import deque


def solution(arr):
    arr = deque(arr)
    res = []
    last_value = arr[-1]
    before_value = arr[0]
    while arr:
        x = arr.popleft()
        if x != before_value:
            res.append(before_value)
            before_value = x
    res.append(last_value)
    return res
