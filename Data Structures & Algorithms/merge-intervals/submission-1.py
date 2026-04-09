class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            start, end = interval
            current_start, current_end = res[-1]
            if current_end >= start:
                res.pop()
                res.append([current_start, max(end, current_end)])
            else:
                res.append(interval)
        return res
        