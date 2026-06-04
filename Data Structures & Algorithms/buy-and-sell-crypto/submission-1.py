class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left_subarray=[0]*len(prices)
        max_right_subarray=[0]*len(prices)
        min_left_subarray[0] = prices[0]
        max_right_subarray[-1] = prices[-1]
        for i in range(1,len(prices)):
            min_left_subarray[i]=min(min_left_subarray[i-1],prices[i])
        for i in range(len(prices)-2,-1,-1):
            max_right_subarray[i]=max(max_right_subarray[i+1],prices[i])
        max_profit=0
        for i in range(0,len(prices)):
            profit=max_right_subarray[i]-min_left_subarray[i]
            if profit>max_profit:
                max_profit=profit
        return(max_profit)

    