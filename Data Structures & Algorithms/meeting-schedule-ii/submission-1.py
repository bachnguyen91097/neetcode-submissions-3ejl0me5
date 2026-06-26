"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_intervals = sorted(intervals, key=lambda i: i.start)
        min_heap = []
        for i in range(len(sorted_intervals)):
            start, end = sorted_intervals[i].start, sorted_intervals[i].end
            if not min_heap:
                heapq.heappush(min_heap, end)
            else:
                if start >= min_heap[0]:
                    heapq.heappop(min_heap)
                
                heapq.heappush(min_heap, end)
        return len(min_heap)
        