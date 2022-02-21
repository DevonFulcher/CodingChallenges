class Solution:
   
    def get_length(self, head):
        length = 0
        while head != None:
            length += 1
            head = head.next
        return length
           
    def fast_forward(self, longer, shorter, node):
        diff = longer - shorter
        for _ in range(diff):
            node = node.next
        return node

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_len = self.get_length(headA)
        b_len = self.get_length(headB)
       
        a_curr = headA
        b_curr = headB
       
        if a_len > b_len:
            a_curr = self.fast_forward(a_len, b_len, a_curr)
        if a_len < b_len:
            b_curr = self.fast_forward(b_len, a_len, b_curr)
           
        while a_curr != None:
            if a_curr == b_curr:
                return a_curr
            a_curr = a_curr.next
            b_curr = b_curr.next
        return None
