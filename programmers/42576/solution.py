def solution(participant, completion):
    hash_dict = {}
    for i in participant:
        hash_dict[i] = hash_dict.get(i, 0) + 1
    for i in completion:
        hash_dict[i] = hash_dict.get(i) - 1
    for key, value in hash_dict.items():
        if value == 1:
            return key
