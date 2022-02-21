# https://leetcode.com/problems/copy-list-with-random-pointer/

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: Node) -> Node:
    if not head:
        return None
    curr = head
    original_to_clone = {}
    while curr:
        original_to_clone[curr] = Node(curr.val)
        curr = curr.next

    for k, v in original_to_clone.items():
        if k.next:
            v.next = original_to_clone[k.next]
        else:
            v.next = None
        if k.random:
            v.random = original_to_clone[k.random]
        else:
            v.random = None

    return original_to_clone[head]
