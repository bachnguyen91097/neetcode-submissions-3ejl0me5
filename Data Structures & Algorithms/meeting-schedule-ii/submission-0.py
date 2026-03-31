"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        minHeap = []
        for interval in intervals:
            if not minHeap:
                heapq.heappush(minHeap, interval.end)
            else:
                head = minHeap[0]
                if head > interval.start:
                    heapq.heappush(minHeap, interval.end)
                else:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, interval.end)
        return len(minHeap)

        