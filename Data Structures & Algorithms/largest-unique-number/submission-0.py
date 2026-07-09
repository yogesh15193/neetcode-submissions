class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        seen=set()
        max_till_now=-1
        for i in nums:
            flag_duplicate=False
            if len(seen)==0:
                seen.add(i)
            elif len(seen)>0 and i in seen and i!=max_till_now:# means this is a 
                pass
            elif len(seen)>0 and i in seen and i==max_till_now:  
                print("hiii")
                flag_duplicate=True
                seen.remove(i)
                print("i",i)
                try:
                    max_till_now=max(seen)
                    seen.add(i)
                except:
                    max_till_now=-1
            else: 
                seen.add(i)
            if flag_duplicate==False: 
                if i>=max_till_now:

            
                    max_till_now=i
            #print(f"max till now {max_till_now} for i={i}")
        return(max_till_now)

            
        