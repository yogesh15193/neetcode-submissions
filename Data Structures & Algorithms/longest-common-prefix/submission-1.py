class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return("")
        if len(strs)==1:
            return strs[-1]
        else:
            candidate=strs[0]
            x=len(candidate)
            k=0
            i=1
            min_prefix_array=[]
            while(i<len(strs)):
                prefix=0
                current_word=strs[i]
                y=len(current_word)
                min_length=min(x,y)
                char=0
                while(char<min_length):
                    if candidate[char]==current_word[char]:
                        prefix+=1
                    else:
                        break
                    char+=1
                min_prefix_array.append(prefix)
                i+=1
            #print(min_prefix_array)
            x=min(min_prefix_array)
            return(candidate[:x])
        
        