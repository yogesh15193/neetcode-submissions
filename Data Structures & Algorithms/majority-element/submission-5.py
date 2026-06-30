class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count1=0
        candidate=None
        for i in nums:
            if i==candidate:
                count1+=1
            elif count1==0:
                candidate=i
                count1=1
            else:
                count1-=1
        return candidate

        