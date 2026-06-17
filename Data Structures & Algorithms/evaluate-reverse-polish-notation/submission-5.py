class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        result=0
        for i in tokens:
            res=0
            flag=False
            try:
                x=int(i)
                stack.append(x)
            except: #We got operator
                elem_1=stack.pop()  # most recent
                elem_2=stack.pop()  # older
                if i=="+":
                    res=elem_2+elem_1
                elif i=="-":
                    res=elem_2-elem_1
                elif i=="*":
                    res=elem_2*elem_1
                else:
                    res=int(elem_2/elem_1)
                # now the result we have gotten, so we update it into the result stack
                #print("res",res)
                stack.append(res)
        return(stack[-1])