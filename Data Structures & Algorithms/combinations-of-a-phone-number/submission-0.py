class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        res = []
        currS = []
        hmap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        self.helper(0, currS, res, digits, hmap)
        return res

    
    def helper(self, i, currS, res, digits, hmap):
        if len(currS) == len(digits):
            res.append("".join(currS))
            return
        if i > len(digits) - 1:
            return
        d_list = hmap[digits[i]]
        for c in d_list:
            currS.append(c)
            self.helper(i+1,currS, res, digits, hmap)
            currS.pop()
        
