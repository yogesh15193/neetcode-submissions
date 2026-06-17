class MinStack:

    def __init__(self):
        self.stack_A=[]
        self.stack_B=[]

    def push(self, val: int) -> None:
        self.stack_A.append(val)
        if len(self.stack_B)>0 :  #checking if minstack is empty or not
            x=self.stack_B[-1]   # top elem of stack_B
            if x>val:   # we found a new min
                self.stack_B.append(val)
            else:
                self.stack_B.append(x)
        else: # stack_B is empty
            self.stack_B.append(val)

    def pop(self) -> None:
        self.stack_A.pop()
        self.stack_B.pop()

    def top(self) -> int:
        return(self.stack_A[-1])

    def getMin(self) -> int:
        return(self.stack_B[-1])
