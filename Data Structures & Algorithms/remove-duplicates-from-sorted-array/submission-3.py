class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                nums[i+1]=nums[j]
                i=i+1 
        nums=nums[0:i+1]
        return(len(nums))