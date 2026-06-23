class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_0=0
        count_1=0
        count_2=0
        for i in nums:
            if i==0:
                count_0+=1
            elif i==1:
                count_1+=1
            else:
                count_2+=1
        nums.clear()
        a,b,c=0,0,0
        #print("nums",nums)
        while(a<count_0):
            nums.append(0)
            a+=1
        while(b<count_1):
            nums.append(1)
            b+=1
        while(c<count_2):
            nums.append(2)
            c+=1
        return(nums)
    
            
        
        