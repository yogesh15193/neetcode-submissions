class Solution:
    def trap(self, height: List[int]) -> int:
        result=0
        max_left=height[0]
        max_right=height[-1]
        for i in range(1,len(height)-1):
            max_left=max(height[0:i])
            max_right=max(height[i+1:])
            water_on_ith=min(max_left,max_right)-height[i]
            if water_on_ith<0:
                water_on_ith=0
            #print("water_on_ith",water_on_ith)
            result=result+water_on_ith
        return result
        