class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        cars=sorted(zip(position,speed),reverse=True)
        for pos,sp in cars:
            time=(target-pos)/sp
            if len(stack)>0 and time>stack[-1]:
                stack.append(time)
            if len(stack)==0:
                stack.append(time)
        return(len(stack))