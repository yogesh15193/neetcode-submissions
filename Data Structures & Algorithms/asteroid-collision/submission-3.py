class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        flag_pos=False
        for i in asteroids:
            if i>0:
                flag_pos=True
            else:
                flag_pos=False
            if len(stack)==0:
                stack.append(i)
            else:
                x=stack[-1]
                if (x>0 and flag_pos==True) or (x<0 and flag_pos==False) or (x<0 and flag_pos==True):
                    stack.append(i)
                elif x>0 and flag_pos==False:
                    if abs(i)>x:
                        stack.pop()
                        while stack:
                            top=(stack[-1])
                            if top<0:
                                stack.append(i)
                                break
                            elif abs(i)>top:
                                    stack.pop()
                            elif abs(i)==top:
                                    stack.pop()
                                    break
                            else:
                                break
                        if len(stack)==0:
                            stack.append(i)
                    elif abs(i)==x:
                        stack.pop()
                    else:
                        pass
            #print(f"{stack} after {i}")    
        return(stack)