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
