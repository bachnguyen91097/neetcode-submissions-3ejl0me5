class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        currentWord = ''
        res = float("inf")
        l,r = 0,0
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1 or wordsDict[i] == word2:
                if len(currentWord) == 0:
                    currentWord = wordsDict[i]
                    l = i
                elif currentWord != wordsDict[i]:
                    r = i
                    res = min(res, r - l)
                    currentWord = wordsDict[i]
                    l = r
                else:
                    l = i
        return res
        