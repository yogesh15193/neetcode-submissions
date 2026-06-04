class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset=set()
        left=0
        right=0
        max_count=0
        count=0
        while right<len(s):
            if s[right] not in myset:
                myset.add(s[right])
                right+=1
            else:
                while s[right] in myset:
                    myset.remove(s[left])
                    left=left+1
                myset.add(s[right])
                right=right+1
            max_count=max(max_count,len(myset))
        return(max_count)    

        