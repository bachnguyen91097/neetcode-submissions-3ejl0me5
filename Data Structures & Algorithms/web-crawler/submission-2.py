# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        res = []
        visited = set()
        def dfs(url):
            if url in visited:
                return
            visited.add(url)
            res.append(url)
            if not htmlParser.getUrls(url):
                return
            for each_url in htmlParser.getUrls(url):
                if each_url[7:].split("/")[0] == url[7:].split("/")[0]:
                    dfs(each_url)
        dfs(startUrl)
        return res
