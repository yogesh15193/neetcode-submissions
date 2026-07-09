class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        dict1={}
        for i in range(len(nums)):
            dict1[nums[i]]=dict1.get(nums[i],0)+1
        #print(dict1)
        max_till_now=-1
        flag=False
        for key,value in dict1.items():
            #print(key,value)
            if key>max_till_now and value==1:
                max_till_now=key
        return(max_till_now)
        