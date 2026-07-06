class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag=False
        flag_last_word_passed=False
        i=len(s)-1
        count=0
        while(i>=0):
            if s[i]==' ' and flag==False:
                pass
            elif s[i]!=' ' and flag_last_word_passed==False:
                flag=True
                count+=1
            if s[i]==' ' and flag==True:
                flag_last_word_passed=True
            i=i-1
        return(count)
                