class MinStack:

    def __init__(self):
        self.st1  = []
        self.st2 = []

    def push(self, val: int) -> None:
        if not self.st1:
            self.st1.append(val)
            self.st2.append(val)
        else:
            minEle = min(self.st2[-1], val)
            print("min ele", minEle)
            self.st1.append(val)
            self.st2.append(minEle)

    def pop(self) -> None:
        self.st1.pop()
        self.st2.pop()

    def top(self) -> int:
        return self.st1[-1]

    def getMin(self) -> int:
        return self.st2[-1]
