from bisect import bisect_left
class MyCalendar:
    
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        i = bisect_left(self.events, [startTime, endTime])

        if i > 0:
            # compare to left neighbor
            s, e = self.events[i-1]
            if startTime < e:
                return False
        if i < len(self.events):
            # compare to right neighbor
            s,e = self.events[i]
            if endTime > s:
                return False
        self.events.insert(i, [startTime, endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)