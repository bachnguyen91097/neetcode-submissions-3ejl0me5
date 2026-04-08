import random
class Solution:

    def __init__(self, w: List[int]):
        self.sumW = sum(w)
        current_sum = 0
        self.prefix_sum = []
        for i in range(len(w)):
            current_sum += w[i]
            self.prefix_sum.append(current_sum)

    def pickIndex(self) -> int:
        random_weight = random.uniform(0,self.sumW)
        for i, prefix_sum in enumerate(self.prefix_sum):
            if prefix_sum >= random_weight:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()