class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i=0
        result=[]
        while(i<len(arr)-1):
            j=i+1
            x=max(arr[j:])
            result.append(x)
            i=i+1
        result.append(-1)
        return(result)
        