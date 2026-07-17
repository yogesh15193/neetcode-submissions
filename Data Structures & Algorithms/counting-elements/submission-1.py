class Solution:
    def countElements(self, arr: List[int]) -> int:
        my_set=set()
        for i in arr:
            if i not in my_set:
                my_set.add(i)
        result=0
        for i in arr:
            if i+1 in my_set:
                result+=1
        return(result)