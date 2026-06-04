class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            nums_left=nums[0:i]
            nums_right=nums[i+1:]
            if len(nums_left)>0:
                res_left=1
                for i in nums_left:
                    res_left=res_left*i
            else:
                res_left=1
            if len(nums_right)>0:
                res_right=1
                for i in nums_right:
                    res_right=res_right*i
            else:
                res_right=1
            res=res_left*res_right
            result.append(res)
        return result



        