class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # O(n^2) for TC since numberAsString += str(digit)
        # numberAsString = ""
        # for digit in digits:
        #     numberAsString += str(digit)
        # res = int(numberAsString) + 1
        # return list(str(res))

        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits