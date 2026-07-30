class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s=list(s)
        freq_dict={}
        for char in s:
            if char in freq_dict:
                freq_dict[char]=freq_dict[char]+1
            else:
                freq_dict[char]=1
        count_odd=0
        for key,value in freq_dict.items():
            val=value
            if val%2!=0:
                count_odd=count_odd+1
            else:
                continue
        if count_odd<=1:
            return True
        else:
            return False
        
        