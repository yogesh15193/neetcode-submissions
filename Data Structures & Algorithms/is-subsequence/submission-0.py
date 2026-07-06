class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        flag=True
        index_s=-1
        index_t=0
        if len(s)>=len(t):
            shorter_string=len(t)
        else:
            shorter_string=len(s)
        i=0
        j=0

        while(i<len(s) and j<len(t)):
            if s[i]==t[j]:
                i=i+1
                j=j+1
            else:
                j=j+1
        if i==len(s):
            return(True)
        else:
            return(False)

            
            
            
    

    
        