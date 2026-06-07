class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d1={}
        for i in range(len(nums)):
            d1[nums[i]]=d1.get(nums[i],0)+1
        max_value=-100000
        #print(d1)
        for k,v in d1.items():
            if v>max_value:
                key_needed=k
                max_value=v
        #print("max_key",k)
        return key_needed


        

        