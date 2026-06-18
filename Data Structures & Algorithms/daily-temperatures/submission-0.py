class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for i in range(len(temperatures)):
            x=temperatures[i]
            try:
                while stack:
                    y=stack[-1]
                    temp_y=temperatures[y]
                    if temp_y<x: # found next warmer day
                        stack.pop()
                        days=i-y
                        result[y]=days
                    else:
                        break
            except:
                pass
            stack.append(i)
            #print(f"{stack} after {i}th iteration")

        return(result)
        
        