class Solution:
    def is_valid(self,count_t, count_s):
        for char, count in count_t.items():
            if count_s.get(char, 0) < count:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        count_t={}
        count_s={}
        min_window_size=100000000
        for i in range(len(t)):
            count_t[t[i]]=count_t.get(t[i],0)+1
        i=0
        j=0
        min_string=''
        current_window=0
        while(j<len(s)):
            count_s[s[j]]=count_s.get(s[j],0)+1
            if (self.is_valid(count_t, count_s)):# window found
                if len(min_string) == 0 or j-i+1 < len(min_string):
                    min_string = s[i:j+1]
                #print("min_string=s[i:j+1] without any deletion",min_string)
                while(i<j and self.is_valid(count_t, count_s)):
                    count_s[s[i]]-=1
                    #print("line 19", count_s.get(s[i]))
                    if not (self.is_valid(count_t, count_s)):
                        #print("at this stage, we must have encountered a character present in t", s[i:j+1])
                        
                        count_s[s[i]]+=1
                        break
                    if len(min_string) == 0 or (j - (i+1) + 1) < len(min_string):
                        min_string = s[i+1:j+1]
                    current_window=len(min_string)
                    i=i+1
                #print("min string after removal of left char",min_string)

                if min_window_size>=current_window:
                    min_window_size=current_window
                j=j+1
                    
            else:
                j=j+1
        return(min_string) 