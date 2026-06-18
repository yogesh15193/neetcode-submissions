class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        candidate=strs[0]
        x=len(candidate)
        k=0
        i=1
        min_length_prefix=100000
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
            min_length_prefix=min(prefix,min_length_prefix)
            i+=1
        return(candidate[:min_length_prefix])
        