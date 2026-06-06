class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]
        i=0
        j=i+k
        max_in_window=0
        while(i< len(nums)-(k-1)):
            max_in_window=max(nums[i:j])
            result.append(max_in_window)
            i+=1
            j+=1
        return result
        