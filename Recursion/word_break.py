from typing import List

def word_break(s: str, words: List[str]) -> bool:
    memo = {}
    def dfs(curr: str):
        if curr in memo:
            return memo[curr]
        if len(curr) > len(s):
            return False
        if curr == s:
            return True
        results = []
        for word in words:
            results.append(dfs(curr + word))
        answer = any(results)
        memo[curr] = answer
        return answer
    return dfs("")
    