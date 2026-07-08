# Trie way
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_subfolder = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        res = []
        folder.sort()
        for f in folder: 
            f_list = f.split("/")[1:] # to not include /
            curr = root
            included = True
            for e in f_list:
                if e not in curr.children:
                    curr.children[e] = TrieNode()
                else:
                    if curr.children[e].is_subfolder:
                        included = False
                curr = curr.children[e]
            curr.is_subfolder = True
            if included:
                res.append(f)
        return res