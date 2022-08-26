from typing import List
import heapq

def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    ans = []
    lists = list(filter(lambda a_list: len(a_list) > 0, lists))
    indices = [(lists[i][0], i, 0) for i in range(len(lists))]
    heapq.heapify(indices)
    while indices:
        val, which_list, list_i = heapq.heappop(indices)
        ans.append(val)
        if list_i+1 < len(lists[which_list]):
            heapq.heappush(indices, (lists[which_list][list_i+1], which_list, list_i+1))
    return ans