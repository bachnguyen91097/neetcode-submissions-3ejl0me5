class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        new_start, new_end = newInterval
        if not intervals:
            intervals.append(newInterval)
        else:
            for i in range(len(intervals)):
                current_start, current_end = intervals[i]
                if current_start >= new_start:
                    intervals.insert(i, newInterval)
        if len(intervals) == n:
            intervals.append(newInterval)
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            curr_start, curr_end = intervals[i]
            prev_start, prev_end = res[-1]
            if curr_start <= prev_end:
                res[-1][1] = max(curr_end, prev_end)
            else:
                res.append(intervals[i])
        return res