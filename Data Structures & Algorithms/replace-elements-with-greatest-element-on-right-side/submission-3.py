class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_till_now=arr[-1]
        arr[-1]=-1
        for i in range(len(arr)-2,-1,-1):
            current_val=arr[i]
            arr[i]=max_till_now
            if max_till_now<=current_val:
                max_till_now=current_val
            
        return(arr)
    