class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        for i in range(0,len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i]<prices[j]:
                    profit=prices[j]-prices[i]
                else:
                    continue
                if profit>max_profit:
                    max_profit=profit
                else:
                    continue
        return(max_profit)
        