class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        if not len(nums)%2==0:
            x=int(len(nums)/2)
            return nums[x]
        else:
            x=int(len(nums)/2)
            return(nums[x-1])
        