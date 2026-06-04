class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1={}
        count_s2={}
        window_size=len(s1)
        for i in range(len(s1)):
            count_s1[s1[i]]=count_s1.get(s1[i],0)+1
        right=0
        left=0
        n=len(s1)
        flag=False
        while(right<len(s2)):
            #print(f"right={right}, window={s2[left:right+1]}, count_s2={count_s2}, count_s1={count_s1}")
            count_s2[s2[right]]=count_s2.get(s2[right],0)+1
            if right-left+1>window_size:
                count_s2[s2[left]] -= 1
                if count_s2[s2[left]] == 0:
                    del count_s2[s2[left]]
                #print(f"in first if, the count_s2 becomes {count_s2}")
                left+=1
            if count_s1==count_s2:
                flag=True
                break
            right+=1
        return flag
        