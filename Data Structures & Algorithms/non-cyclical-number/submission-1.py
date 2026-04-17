class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        if n == 1:
            return True
        num = n
        while num != 1:
            curr = 0
            n_string = str(num)
            for c in n_string:
                curr += int(c) ** 2
            if curr in seen:
                return False
            seen.add(curr) 
            num = curr
        return True       