class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        j=0
        count=0
        while(i<len(s) and j<len(t)):
            if s[i]==t[j]:
                count+=1
                i=i+1
                j=j+1
            else:
                i=i+1
        string_to_be_added=t[count:]
        s_new=s+string_to_be_added
        output=len(t)-count
        return output

        