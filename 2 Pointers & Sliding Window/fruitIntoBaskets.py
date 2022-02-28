from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        num_types = 0
        num_baskets = 2
        l, r = 0, 0
        fruit_count = defaultdict(int)
        max_fruit = 0
        while r < len(fruits):
            while num_types <= num_baskets:
                if fruit_count[fruits[r]] == 0:
                    num_types += 1
                fruit_count[fruits[r]] += 1
                r += 1
                if num_types <= num_baskets:
                    max_fruit = max(r-l, max_fruit)
                if r >= len(fruits):
                    return max_fruit
            fruit_count[fruits[l]] -= 1
            if fruit_count[fruits[l]] == 0:
                num_types -= 1
            l += 1