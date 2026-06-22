class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        if len(nums)==0:
            return -1
        if len(nums)==1 and target!=nums[-1]:
            return -1
        else:
            mid_elem=(i+j)//2
            x=nums[mid_elem]
            if x==target:
                return mid_elem
            if x<target:
                result=self.search(nums[mid_elem+1::],target)
                if result==-1:
                    return -1
                else:
                    return result+mid_elem+1
                
            if x>target:
                return(self.search(nums[0:mid_elem],target))
            