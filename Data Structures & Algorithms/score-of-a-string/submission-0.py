class Solution:
    def scoreOfString(self, s: str) -> int:
        output=0
        i=0
        j=i+1
        while(i<len(s)-1):
            diff=abs(ord(s[j])-ord(s[i]))
            output=output+diff
            i=i+1
            j=j+1
        return(output)

        