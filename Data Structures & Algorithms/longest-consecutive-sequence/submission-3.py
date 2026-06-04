class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_unique=list(set(nums))
        counter=0
        counter_in_loop=0
        max_long_subsequence=0
        for i in range(len(nums_unique)):
            print("current i:", nums_unique[i])
            if nums_unique[i]-1 in nums_unique: 
                continue
            else:
                print(f"in else with nums_unique {nums_unique[i]}")
                counter_in_loop=1   # i-1 is not in the list, so anchor can be i
                current=nums_unique[i]
                print("counter in loop when enters else", counter_in_loop)
                while current+1 in nums_unique:
                    print(f"in while loop with {nums_unique[i]}")
                    counter_in_loop+=1
                    print("counter in loop", counter_in_loop)
                    current=current+1
                    
                counter=counter_in_loop
                if counter>=max_long_subsequence:
                    max_long_subsequence=counter
                
            print(f" current i after iteration {i}")
            
            
        return(max_long_subsequence)
        