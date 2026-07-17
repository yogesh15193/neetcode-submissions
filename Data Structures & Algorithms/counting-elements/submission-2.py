class Solution:
    def countElements(self, arr: List[int]) -> int:
        my_set=set(arr)
        result=0
        for i in arr:
            if i+1 in my_set:
                result+=1
        return(result)