from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    while progresses:
        for idx in range(len(progresses)):
            progresses[idx] = progresses[idx] + speeds[idx]

        cnt = 0
        for idx in range(len(progresses)):
            if progresses[idx] >= 100:
                cnt += 1
            else:
                break
        for i in range(cnt):
            progresses.popleft()
            speeds.popleft()

        if cnt > 0:
            answer.append(cnt)

    return answer
