class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue
            start, end = interval
            top_start, top_end = stack[-1]

            if top_end > start:
                stack.pop()
                stack.append((top_start, min(end, top_end)))
            else:
                stack.append(interval)
        return len(intervals) - len(stack)