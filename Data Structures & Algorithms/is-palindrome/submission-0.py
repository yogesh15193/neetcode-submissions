import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ", "")
        s=re.sub(r'[^a-z0-9]','',s)
        print("original string", s)
        print("reversed string",s[::-1])
        if s==s[::-1]:
            return True
        else:
            return False
