class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(0,n+1):
            cnt = 0
            while i > 0:
                if i & 1 == 1:
                    cnt += 1
                i = i >> 1
            output.append(cnt)
        return output
            
