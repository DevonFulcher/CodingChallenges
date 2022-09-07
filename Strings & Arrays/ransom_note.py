# https://leetcode.com/problems/ransom-note/solution/

class Solution:
    from collections import Counter
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        
        for char in ransomNote:
            if char not in mag_count or mag_count[char] == 0:
                return False
            mag_count[char] -= 1
            
        return True