class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict={}
        for number in nums:
            my_dict[number]=my_dict.get(number,0)+1
        print("hello")
        print(my_dict)
        for keys,values in my_dict.items():
            if values!=1:
                return True
        return False