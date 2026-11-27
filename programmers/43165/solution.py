res = 0


def dfs(numbers, target, cnt, value):
    global res
    if cnt == len(numbers):
        if value == target:
            res += 1
        return

    dfs(numbers, target, cnt + 1, value + numbers[cnt])
    dfs(numbers, target, cnt + 1, value - numbers[cnt])


def solution(numbers, target):
    global res
    res = 0

    dfs(numbers, target, 0, 0)
    return res
