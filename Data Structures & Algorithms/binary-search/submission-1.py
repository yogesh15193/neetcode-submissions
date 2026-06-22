class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        flag=False
        while(left<=right):
            mid=(left+right)//2
            if target==nums[mid]:
                flag=True
                return mid
            if nums[mid]<target:
                left=mid+1
            if nums[mid]>target:
                right=mid-1
           
        if flag==False:
            return -1


        