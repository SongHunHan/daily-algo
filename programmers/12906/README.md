# 12906. 같은 숫자는 싫어

같은 숫자가 연달아 나오면 하나만 남기고 원래 순서를 유지한다. 예를 들어 `[2, 2, 5, 2]`의 결과는 `[2, 5, 2]`다. 마지막 `2`는 `5` 뒤에 다시 나왔으므로 남긴다. [문제 원문](https://school.programmers.co.kr/learn/courses/30/lessons/12906)

## 큐(Queue)

큐는 먼저 넣은 값부터 꺼내는 자료구조다(FIFO). Python의 `deque`를 큐로 쓸 때는 `append(x)`로 오른쪽 끝에 넣고 `popleft()`로 왼쪽 끝에서 꺼낸다.

## 풀이

`popleft()`로 숫자를 하나씩 꺼낸다. 꺼낸 숫자가 `before_value`와 다르면 직전 숫자의 묶음이 끝난 것이므로 `before_value`를 결과에 넣고 새 숫자를 기억한다. 마지막 묶음 뒤에는 비교할 숫자가 없으므로 반복이 끝난 뒤 `last_value`를 한 번 넣는다.

[Python 풀이 보기](solution.py)
