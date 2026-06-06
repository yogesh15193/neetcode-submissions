class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result=[]
        result.append(-1)
        print(result)
        max_till_now=0
        for i in range(len(arr)-2,-1,-1):
            if arr[i+1]>max_till_now:
                max_till_now=arr[i+1]
            result.append(max_till_now)
        #print(result)
        return(result[::-1])