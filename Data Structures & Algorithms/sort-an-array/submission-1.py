class Solution:
    def quicksort(self,nums):
        length=len(nums)
        if length<=1:
            return nums
        else:
            x=length//2
            pivot=nums.pop(x)
            less_than_pivot=[]
            greater_than_pivot=[]
            for i in nums:
                if i<=pivot:
                    less_than_pivot.append(i)
                else:
                    greater_than_pivot.append(i)
            return (self.quicksort(less_than_pivot) + [pivot] + self.quicksort(greater_than_pivot))               
    def sortArray(self, nums: List[int]) -> List[int]:
        result=self.quicksort(nums)
        return result
        