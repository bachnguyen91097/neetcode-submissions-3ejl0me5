class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int) -> None:
        if not self.stack2:
            self.stack2.append(val)
        else:
            topStack2 = self.stack2[-1]
            if topStack2 >= val:
                self.stack2.append(val)
        self.stack1.append(val)

    def pop(self) -> None:
        if self.stack1:
            poppedItem = self.stack1[-1]
        if self.stack2 and poppedItem == self.stack2[-1]:
            self.stack2.pop()
        self.stack1.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1]
        
