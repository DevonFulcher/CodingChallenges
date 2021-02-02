# https://leetcode.com/problems/random-pick-with-weight/
import random


class Solution:

    def __init__(self, w: list[int]):
        w_sum = sum(w)
        probabilities = list(map(lambda x: x / w_sum, w))
        self.ranges = []
        lower_range = 0
        for prob in probabilities:
            upper_range = lower_range + prob
            self.ranges.append((lower_range, upper_range))
            lower_range = upper_range

    def pickIndex(self) -> int:
        rand_float = random.uniform(0, 1)
        for i, (lower, upper) in enumerate(self.ranges):
            if rand_float >= lower and rand_float < upper:
                return i
