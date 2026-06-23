class Solution:
    def quicksort(self,nums):
        if len(nums)==0:
            return []
        if len(nums)==1:
            return nums
        else:
            pivot=nums[-1]
            greater_than_pivot=[]
            less_than_pivot=[]
            for i in range(0,len(nums)-1):
                if nums[i]>=pivot:
                    greater_than_pivot.append(nums[i])
                else:
                    less_than_pivot.append(nums[i])
            return self.quicksort(less_than_pivot)+[pivot]+self.quicksort(greater_than_pivot)
    def sortColors(self, nums: List[int]) -> None:
        nums[:] = self.quicksort(nums)
        return nums
        
        