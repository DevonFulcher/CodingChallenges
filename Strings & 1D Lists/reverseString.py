# https://leetcode.com/problems/reverse-string/

def reverseString(s: list[str]) -> None:
    if not list:
        return None
    l_index, r_index = 0, len(s)-1
    while l_index < r_index:
        s[l_index], s[r_index] = s[r_index], s[l_index]
        l_index += 1
        r_index -= 1
