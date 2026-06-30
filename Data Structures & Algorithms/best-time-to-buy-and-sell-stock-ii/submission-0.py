class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        stock_bought=False
        for i in range(1,len(prices)):
            temp_profit=0
            if prices[i]>prices[i-1]: # buy
                buy_stock_price=prices[i-1]
                stock_bought=True
            else:
                pass
            if stock_bought==True:
                temp_profit=prices[i]-buy_stock_price
                stock_bought=False
            profit=profit+temp_profit
            #print(profit)
        return(profit)
                