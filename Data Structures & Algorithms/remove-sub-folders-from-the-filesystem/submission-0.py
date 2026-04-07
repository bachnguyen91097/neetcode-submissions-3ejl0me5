class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        res.append(folder[0])
        for i in range(1,len(folder)):
            if folder[i].startswith(res[-1] + "/"):
                continue
            res.append(folder[i])
        return res

