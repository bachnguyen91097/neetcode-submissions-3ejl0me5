class Solution:
    def simplifyPath(self, path: str) -> str:
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
        return "/" + "/".join(stack)