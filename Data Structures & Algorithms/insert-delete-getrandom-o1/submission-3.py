import random
class RandomizedSet:

    def __init__(self):
        self.dictRandomizedSet = {}
        self.dictArray = []

    def insert(self, val: int) -> bool:
        if val in self.dictRandomizedSet:
            return False
        self.dictArray.append(val)
        self.dictRandomizedSet[val] = len(self.dictArray) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dictRandomizedSet:
            return False
        index_remove_val = self.dictRandomizedSet[val]
        last_ele = self.dictArray[-1]
        last_index = len(self.dictArray) - 1
        self.dictArray[last_index], self.dictArray[index_remove_val] = self.dictArray[index_remove_val], self.dictArray[last_index]
        self.dictRandomizedSet[last_ele] = index_remove_val
        self.dictArray.pop()
        del self.dictRandomizedSet[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.dictArray)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()