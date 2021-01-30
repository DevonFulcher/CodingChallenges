# https://leetcode.com/problems/longest-palindrome/

import collections


def longestPalindrome(s):
    letterToCount = collections.Counter(s)
    answer = 0
    for key in letterToCount:
        answer += letterToCount[key] // 2 * 2
    if answer != len(s):
        answer += 1
    return answer
