class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_till_now=0
        i=0
        j=0
        count=0
        while(j<len(nums)):
            flag=True
            if nums[j]==1 and flag==True:
                count=count+1
                print("count ", count)
            else:
                i=j+1
                flag=False
                count=0
            if count>max_till_now:
                max_till_now=count
            #print(f"{max_till_now} at {j}")
            j=j+1
        return(max_till_now)
         
        