class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=i+1
        while(j<len(nums)):
            if nums[j]!=nums[i]:
                i=i+1
                j=j+1
            else:
                nums.pop(j)
        k=len(nums)
        return(k)