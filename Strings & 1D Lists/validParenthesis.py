class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        leftTokens = set(["(", "{", "["])
        for char in s:
            if char in leftTokens:
                stack.append(char)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if char == ")" and popped != "(":
                    return False
                if char == "}" and popped != "{":
                    return False
                if char == "]" and popped != "[":
                    return False
        return not stack