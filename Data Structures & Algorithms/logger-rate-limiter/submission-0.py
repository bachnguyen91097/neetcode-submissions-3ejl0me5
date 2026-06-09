class Logger:

    def __init__(self):
        self.hmap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.hmap and timestamp < self.hmap[message]:
            return False
        self.hmap[message] = timestamp + 10
        return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
