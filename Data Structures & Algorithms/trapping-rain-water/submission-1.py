class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_arr=[0]*len(height)
        max_right_arr=[0]*len(height)
        result=0
        for i in range(1,len(height)):
            max_left_arr[i]=max(max_left_arr[i-1],height[i-1])
        for i in range(len(height)-2, -1, -1):
            max_right_arr[i] = max(max_right_arr[i+1], height[i+1])
        for i in range(1,len(height)-1):
            water_on_ith_index=min(max_left_arr[i],max_right_arr[i])-height[i]
            if water_on_ith_index<0:
                water_on_ith_index=0
            result=result+water_on_ith_index
        return result
        
        