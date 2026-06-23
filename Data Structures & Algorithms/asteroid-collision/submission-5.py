class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            while stack and stack[-1]>0 and i<0:
                difference=i+stack[-1]
                if difference<0:
                    stack.pop()
                elif difference>0:
                    i=0
                else:
                    i=0
                    stack.pop()
            if i!=0:
                stack.append(i)
        return stack
        