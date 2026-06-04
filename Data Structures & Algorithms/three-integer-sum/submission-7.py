class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            k=i+1
            j=len(nums)-1
            curr=nums[i]
            while(k<j):
                sum_two_pointers=nums[k]+nums[j]
                if curr+sum_two_pointers==0:
                    temp=[]
                    temp.append(nums[i])
                    temp.append(nums[j])
                    temp.append(nums[k])
                    result.append(temp)
                    k=k+1
                    j=j-1
                    while(k<j) and nums[k]==nums[k-1]:
                        k=k+1                           #skipping k
                    while(k<j) and nums[j]==nums[j+1]:
                        j=j-1   
                elif curr+sum_two_pointers<0:
                    k+=1
                else:
                    j-=1
                
            #print(f"{result} for {i}th iteration")
        return(result)
        