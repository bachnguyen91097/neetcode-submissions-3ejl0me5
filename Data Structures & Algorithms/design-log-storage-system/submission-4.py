class LogSystem:

    def __init__(self):
        self.hmap = defaultdict(list)
        self.idx = {
        "Year": 4,
        "Month": 7,
        "Day": 10,
        "Hour": 13,
        "Minute": 16,
        "Second": 19
    }

    def put(self, id: int, timestamp: str) -> None:
        self.hmap[timestamp].append(id)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        res = []
        modified_start = start[:self.idx[granularity]]
        modified_end = end[:self.idx[granularity]]
        for key in self.hmap:
            idsList = self.hmap[key]
            modified_key = key[:self.idx[granularity]]

            if modified_start <= modified_key <= modified_end:
                res.extend(idsList)
        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
