# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        list_len = 0
        curr = head
        while curr:
            list_len += 1
            curr = curr.next
        
        curr = head
        for _ in range(list_len//2):
            stack.append(curr.val)
            curr = curr.next
        
        if list_len % 2 != 0:
            curr = curr.next
        
        while curr:
            if stack.pop() != curr.val:
                return False
            curr = curr.next
        
        return True