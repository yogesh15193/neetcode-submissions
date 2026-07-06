class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        zeroes_nums=[0]*len(nums)
        for i in nums:
            value=i-0
            if value>0 and value<len(nums)+1:
                zeroes_nums[value-1]=1
            else:
                pass
        #print(zeroes_nums)
        number=1
        flag_found=False
        for i in range(len(zeroes_nums)):
            if zeroes_nums[i]==0:
                flag_found=True
                return(number)
                break
            else:
                pass
            number+=1
        if flag_found==False:
            return(number)
        