import itertools
import operator
import functools

with open("input.txt", "r") as f:
    numbers = [int(num) for num in list(f)]


def get_answer(num_combinations):
    comb = list(itertools.combinations(numbers, num_combinations))
    result = list(filter(lambda nums: sum(nums) == 2020, comb))[0]
    return functools.reduce(operator.mul, result)

print(f"Part 1: {get_answer(2)}")
print(f"Part 2: {get_answer(3)}")