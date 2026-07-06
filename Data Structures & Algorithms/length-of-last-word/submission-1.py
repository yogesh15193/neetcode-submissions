class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag=False
        count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                pass
            else:
                flag=True
                while(s[i]!=' ' and i>=0):
                    count+=1
                    i=i-1
                break

        return count
                    
