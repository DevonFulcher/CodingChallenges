# https://leetcode.com/problems/longest-palindrome/

import collections
'''
abccccdd

{
    a: 1
    b: 1
    c: 4
    d: 2
}
'''

def longestPalindrome(s):
    letterToCount = collections.Counter(s)
    answer = 0
    usedOddWord = False
    for key in letterToCount:
        if not usedOddWord and letterToCount[key] % 2 == 1:
            answer += 1
            usedOddWord = True
        answer += letterToCount[key] // 2 * 2
    return answer

def longestPalindromeImproved(s):
    letterToCount = collections.Counter(s)
    answer = 0
    for key in letterToCount:
        answer += letterToCount[key] // 2 * 2
    if answer != len(s):
        answer += 1
    return answer