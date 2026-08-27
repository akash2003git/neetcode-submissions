class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = 0

    def push(self, val: int) -> None:
         if not self.stack:
            self.stack.append(0)
            self.mini = val
         else:
            self.stack.append(val - self.mini)
            if val < self.mini:
                self.mini = val

    def pop(self) -> None:
        pop = self.stack.pop()     
        if pop < 0:
            self.mini -= pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return self.mini + top
        else:
            return self.mini

    def getMin(self) -> int:
        return self.mini
