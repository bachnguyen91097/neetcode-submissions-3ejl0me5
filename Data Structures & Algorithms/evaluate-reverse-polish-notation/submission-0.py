class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def helper(n1, n2, operator):
            if operator == "+":
                return n1 + n2
            elif operator == '-':
                return n2 - n1
            elif operator == '*':
                return n1 * n2
            else:
                return int(n2 / n1)
        numberStack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                numberStack.append(int(token))
            else:
                n1 = numberStack.pop()
                n2 = numberStack.pop()
                result = helper(n1, n2, token)
                numberStack.append(result)
        return numberStack[-1]
