class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
                pass
            else:
                while(nums[i] != i+1 and (nums[i]>=1 and nums[i]<=len(nums)) and nums[i]!=nums[nums[i]-1]):
                    right_index_for_this_number=nums[i]
                    nums[right_index_for_this_number-1],nums[i]=nums[i],nums[right_index_for_this_number-1]
                    
            #print(f"{nums} after i={i}")
        flag=False
        for j in range(len(nums)):
            if j+1!=nums[j]:
                return(j+1)
            else:
                continue
        if flag==False:
            return nums[i]+1


        