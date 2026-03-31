class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        i = 1
        while i < len(intervals):
            if intervals[i-1].end > intervals[i].start:
                return False
            i += 1
        return True