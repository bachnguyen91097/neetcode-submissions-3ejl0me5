class HitCounter:

    def __init__(self):
        self.dict_hit = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.dict_hit[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        cnt = 0
        start_time = timestamp - 300 + 1
        for timestamp in range(start_time, timestamp+1):
            cnt += self.dict_hit[timestamp]
        return cnt


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
