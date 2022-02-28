# https://leetcode.com/problems/meeting-rooms-ii/

# space: O(n), time: O(nlogn)

def minMeetingRooms(intervals: list[list[int]]) -> int:
    import heapq
    if len(intervals) == 1:
        return 1
    answer = 1
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    # add the first interval's end time to the heap
    heap = [sorted_intervals[0][1]]
    for interval in sorted_intervals[1:]:
        earliest_end_time = heapq.nsmallest(1, heap)[0]
        if interval[0] < earliest_end_time:
            heapq.heappush(heap, interval[1])
            answer += 1
        else:
            heapq.heapreplace(heap, interval[1])
    return answer


minMeetingRooms([[13, 15], [1, 13]])

####################################
# Implementation 2
####################################

import heapq
from typing import List
class Solution:
    '''
    sort intervals
    pop from heap == lastMeeting
    if curr start > lastMeeting, don't add to numRooms
    else add + 1 to numRooms and push lastMeeting back on to heap
    add curr to min-heap by end time
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        def interval_to_heap_item(interval):
            return (interval[1], interval[0])
       
        def heap_item_to_interval(heap_item):
            return [heap_item[1], heap_item[0]]
       
        sorted_ints = sorted(intervals, key=lambda i: i[0])
        meetings_heap = []
        num_rooms = 1
        for interval in sorted_ints:
            if meetings_heap:
                lastMeeting = heap_item_to_interval(heapq.heappop(meetings_heap))
                if interval[0] < lastMeeting[1]:
                    num_rooms += 1
                    heapq.heappush(meetings_heap, interval_to_heap_item(lastMeeting))
            heapq.heappush(meetings_heap, interval_to_heap_item(interval))
        return num_rooms
