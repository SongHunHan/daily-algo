from itertools import product, permutations, combinations


def solution(clothes):
    cloth_dict = {}
    for i, cloth_type in clothes:
        cloth_dict[cloth_type] = cloth_dict.get(cloth_type, 0) + 1

    res = 1
    for value in cloth_dict.values():
        res *= (value + 1)

    return res - 1
