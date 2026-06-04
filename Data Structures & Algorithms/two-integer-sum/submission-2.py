class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1={}
        for position,value in enumerate(nums):
            complement=target-value
            if complement in d1:
                return[d1[complement],position]
            else:
                d1[value]=position
        
        