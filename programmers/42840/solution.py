def solution(answers):
    answer = []
    per_1, cnt_1 = [1, 2, 3, 4, 5], 0
    per_2, cnt_2 = [2, 1, 2, 3, 2, 4, 2, 5], 0
    per_3, cnt_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], 0

    for idx, i in enumerate(answers):
        per_1_idx = idx % len(per_1)
        if per_1[per_1_idx] == i:
            cnt_1 += 1

        per_2_idx = idx % len(per_2)
        if per_2[per_2_idx] == i:
            cnt_2 += 1

        per_3_idx = idx % len(per_3)
        if per_3[per_3_idx] == i:
            cnt_3 += 1

    max_cnt = max(cnt_1, cnt_2, cnt_3)

    for idx, i in enumerate([cnt_1, cnt_2, cnt_3]):
        if i == max_cnt:
            answer.append(idx + 1)

    return answer
