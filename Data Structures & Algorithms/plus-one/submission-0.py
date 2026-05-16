class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numberAsString = ""
        for digit in digits:
            numberAsString += str(digit)
        res = int(numberAsString) + 1
        return list(str(res))