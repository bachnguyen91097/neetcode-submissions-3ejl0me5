class Solution:
    def simplifyPath(self, path: str) -> str:
        # print(path.split("/"))
        path_list = path.split("/")
        stack = []
        for element in path_list:
            if element == "" or element == ".":
                continue
            elif element == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(element)
        # print("/".join(path.split("/")))
        return "/" + "/".join(stack)