class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        
        flag=False
        while(i<len(nums)-1):
            j=i+1
            while(j<len(nums)):
                if nums[j]==nums[i] and j-i<=k:
                    flag=True
                    return True
                j=j+1
            i=i+1
        if flag==False:
            return False
    
        