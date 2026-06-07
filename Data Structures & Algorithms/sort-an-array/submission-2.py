class Solution:
    def quicksort(self,nums):
        length=len(nums)
        if len(nums)<=1:
            return nums
        else:
            piv_index=int(length//2)
            pivot=nums[piv_index]
            nums.pop(piv_index)
            elements_less_pivot=[]
            elements_greater_pivot=[]
            for i in nums:
                if i<=pivot:
                    elements_less_pivot.append(i)
                else:
                    elements_greater_pivot.append(i)
            return (self.quicksort(elements_less_pivot))+[pivot]+(self.quicksort(elements_greater_pivot))

        
    def sortArray(self, nums: List[int]) -> List[int]:
        return(self.quicksort(nums))
        