class MyQueue:

    def __init__(self):
        self.stack=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        i=0
        n=len(self.stack)
        if len(self.stack2)==0:
            while(i<n):
                x=self.stack.pop()
                self.stack2.append(x)
                i+=1
            return(self.stack2.pop())
        else:
            return self.stack2.pop()


    def peek(self) -> int:
        if len(self.stack2)>0:
            return self.stack2[-1]
        else:
            i=0
            n=len(self.stack)
            while(i<n):
                x=self.stack.pop()
                self.stack2.append(x)
                i+=1
            peak=self.stack2[-1]
            return peak
        
        

    def empty(self) -> bool:
        if len(self.stack)==0 and len(self.stack2)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()