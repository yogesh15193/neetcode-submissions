#cleaner code
class Solution:
    def is_valid(self,count_t, count_s):
        for char, count in count_t.items():
            if count_s.get(char, 0) < count:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        count_s = {}
        min_string = ''
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        left = 0
        right = 0
        while right < len(s):
            count_s[s[right]] = count_s.get(s[right], 0) + 1
            while self.is_valid(count_t, count_s):
                if len(min_string) == 0 or right - left + 1 < len(min_string):
                    min_string = s[left:right+1]
                count_s[s[left]] -= 1
                left += 1
            right += 1
        return(min_string)