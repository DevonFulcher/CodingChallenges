# https://algo.monster/problems/permutations

from typing import List

def permutations(letters: str) -> List[str]:
    result = []
    def dfs(curr_perm, curr_letters):
        if not curr_letters:
            result.append(curr_perm)
            return
        for i, _ in enumerate(curr_letters):
            next_letters = curr_letters[:i] + curr_letters[i+1:]
            dfs(curr_perm + curr_letters[i], next_letters)
    dfs("", letters)
    return result
    