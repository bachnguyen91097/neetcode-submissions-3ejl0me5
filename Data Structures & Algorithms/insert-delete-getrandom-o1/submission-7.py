class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hmap = {}

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        self.hmap[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hmap:
            return False
        idx_val = self.hmap[val]
        last_val_arr = self.arr[-1]
        self.arr[idx_val] = last_val_arr
        self.hmap[last_val_arr] = idx_val
        self.arr.pop()
        del self.hmap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()