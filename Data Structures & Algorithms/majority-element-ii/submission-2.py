class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        threshold=n//3
        count1=0
        count2=0
        candidate1=None
        candidate2=None
        for i in nums:
            if i==candidate1:
                count1+=1
            elif i==candidate2:
                count2+=1
            elif count1==0:
                candidate1=i
                count1=1
            elif count2==0:
                candidate2=i
                count2=1
            else:
                count1-=1
                count2-=1
        x=nums.count(candidate1)
        y=nums.count(candidate2)
        print("threshold", threshold)
        x_bool=False
        y_bool=False
        if x>threshold:
            x_bool=True
        if y>threshold:
            y_bool=True
        print(x_bool,y_bool)
        if x_bool and y_bool:
            return [candidate1,candidate2]
        if x_bool and not y_bool:
            return[candidate1]
        else:
            return[]

        