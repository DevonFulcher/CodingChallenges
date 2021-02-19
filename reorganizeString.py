# https://leetcode.com/problems/reorganize-string/

from collections import Counter
import math
import heapq


class HeapItem:

    def __init__(self, letter, occurrence):
        self.letter = letter
        self.occurrence = occurrence

    def __lt__(self, other):
        # This is for a max-heap so this comparison is the inverse of what you would expect
        return self.occurrence > other.occurrence


class Solution:
    '''
    aaabbc
    a -> 3
    b -> 2
    c -> 1
    abcaba
    aaabb

    aaabc

    abaca
    abcaa
    1. transform S into a counter object
    2. if any of the values of the counter are greater than the ceiling of half the length of the S, return ""
    3. insert counter items into max-heap with the values being the indices
    4. while the heap isn't empty (the popped item count isn't 0), pop the root, if the letter is equal to the last item in the result then pop the root again, add these letters to the result
    5. decrement the count associated with these letters and push them back onto the heap
    '''

    def reorganizeString(self, S: str) -> str:
        count = Counter(S)
        count_items = count.items()
        for letter, occurrence in count_items:
            if occurrence > math.ceil(len(S) / 2):
                return ""

        def add_to_result(item, heap, result):
            result.append(item.letter)
            item.occurrence -= 1
            heapq.heappush(heap, item)

        result = []
        prev = None
        heap = list(map(lambda item: HeapItem(item[0], item[1]), count_items))
        top = heapq.heappop(heap)
        while top.occurrence > 0:
            if top.letter == prev:
                second = heapq.heappop(heap)
                add_to_result(second, heap, result)
            add_to_result(top, heap, result)
            prev = top.letter
            top = heapq.heappop(heap)

        return "".join(result)


s = Solution()
s.reorganizeString("baaba")
