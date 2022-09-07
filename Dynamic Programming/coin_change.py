# https://leetcode.com/problems/coin-change/submissions/

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(memo, curr_amount):
            if curr_amount in memo:
                return memo[curr_amount]
            if curr_amount == amount:
                return 0
            if curr_amount > amount:
                return -1
            results = []
            for coin in coins:
                result = helper(memo, curr_amount + coin)
                if result != -1:
                    results.append(1 + result)
            if not results:
                memo[curr_amount] = -1
                return -1
            memo[curr_amount] = min(results)
            return memo[curr_amount]
        return helper({}, 0)
