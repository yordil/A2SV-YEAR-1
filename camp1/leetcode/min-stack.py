class MinStack:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # self.minn[val] +=1
        if self.stack2 and self.stack[self.stack2[-1] -1] >= val:
            self.stack2.append(len(self.stack))
        elif not self.stack2:
            self.stack2.append(len(self.stack))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            if len(self.stack) < self.stack2[-1]:
                self.stack2.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return 

    def getMin(self) -> int:
        if self.stack:
            return self.stack[self.stack2[-1] -1 ] 
        else:
            return


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()