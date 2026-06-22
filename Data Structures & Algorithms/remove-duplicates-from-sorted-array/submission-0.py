class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=i+1
        while(j<len(nums)):
            if nums[j]==nums[i]:
                nums.pop(j)
            else:
                i+=1
                j+=1
        k=len(nums)
        return(k)
