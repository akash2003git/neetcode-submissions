class MinStack:

    def __init__(self):
        self.min = float('-inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val   

    def pop(self) -> None:
        if self.stack[-1] < 0:
            self.min = self.min - self.stack.pop()
        else:
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min
        else:
            return self.stack[-1] + self.min
 
    def getMin(self) -> int:
        return self.min
        
