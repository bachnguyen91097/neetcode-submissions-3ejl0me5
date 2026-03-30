# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return n
        start = 0
        end = n - 1
        while start <= end:
            m = start + (end - start) // 2
            if guess(m) == -1:
                end = m - 1
            elif guess(m) == 1:
                start = m + 1
            else:
                return m
        return n
        