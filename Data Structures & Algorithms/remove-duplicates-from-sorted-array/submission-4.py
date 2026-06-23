class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=1
        right=1
        for i in range(right,len(nums)):
            if nums[right]==nums[right-1]:
                right=right+1
            elif nums[right]!=nums[right-1]:
                nums[left]=nums[right]
                left=left+1
                right=right+1

        return(len(nums[0:left]))
