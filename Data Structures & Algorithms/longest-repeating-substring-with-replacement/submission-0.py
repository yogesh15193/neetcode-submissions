class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        right=0
        result=0
        length_window=0
        left=0
        while(right<len(s)):
            #print("iteration", right)
            count[s[right]]=count.get(s[right],0)+1 #A gets into the hash
            length_window+=1
            if length_window-max(count.values())<=k:
                right=right+1
                result=length_window
                result=max(result,length_window)
                #print(f"result got tested after {right}th iteration which is {result}")
            else:
                #print(f"in else during right={right}th iteration")
                count[s[left]]=count[s[left]]-1
                #print("count", count)
                left=left+1
                right=right+1
                length_window=length_window-1
        return result