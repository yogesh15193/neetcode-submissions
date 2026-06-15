class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        d1 = {}
        flag=True
        for close, open in zip(closing, opening):
            d1[close] = open
        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if len(stack)>0:
                    x=stack.pop()
                else:
                    flag=False
                    break
                if d1[i]!=x:
                    flag=False
                else:
                    continue
        if len(stack)>0:
            flag=False
        return flag
            
        
        