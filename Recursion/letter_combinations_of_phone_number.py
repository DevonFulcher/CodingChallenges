# https://algo.monster/problems/letter_combinations_of_phone_number

from typing import List

def letter_combinations_of_phone_number(digits: str) -> List[str]:
    phone = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    result = []
    def dfs(path, curr_digits):
        if not curr_digits:
            result.append("".join(path))
            return
        if curr_digits[0] == "1":
            dfs(path, curr_digits[1:])
            return
        for letter in phone[curr_digits[0]]:
            path.append(letter)
            dfs(path, curr_digits[1:])
            path.pop()
    dfs([], digits)
    return result
    