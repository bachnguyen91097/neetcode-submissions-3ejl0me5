class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda i: i[0])

        res = [sorted_intervals[0]]

        for i in range(1,len(sorted_intervals)):
            current_start, current_end = sorted_intervals[i]
            prev_start, prev_end = res[-1]
            if current_start <= prev_end:
                res[-1][1] = max(current_end, prev_end)
            else:
                res.append(sorted_intervals[i])
        
        return res
            