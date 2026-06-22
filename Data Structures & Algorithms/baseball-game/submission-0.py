class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        res=0
        for i in operations:
            try:
                x=int(i)
                stack.append(x)
            except:
                if i=='+':
                    y=stack.pop()
                    x=stack.pop()
                    z=x+y
                    stack.append(x)
                    stack.append(y)
                    stack.append(z)
                if i=='D':
                    x=stack.pop()
                    double=2*x
                    stack.append(x)
                    stack.append(double)
                if i=='C':
                    stack.pop()
            #print(f"{stack} after {i}")
        for i in stack:
            res=res+i
        return(res)
        