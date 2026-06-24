class StockSpanner:

    def __init__(self):
        self.stack_prices=[]
        self.stack_days=[]
    def next(self, price: int) -> int:
        output=[]
        count_days=1
        if (len(self.stack_prices) and len(self.stack_days))==0: # first price is always 1
            self.stack_prices.append(price)
            self.stack_days.append(count_days)
            output.append(count_days)
            return count_days
        else:
            x=self.stack_prices[-1]
            if x>price:
                self.stack_prices.append(price)
                self.stack_days.append(count_days)
                output.append(count_days)
                return count_days
            else:
                total_days=0
                while (self.stack_prices and self.stack_prices[-1]<=price):
                    self.stack_prices.pop()
                    days=self.stack_days.pop()
                    total_days=total_days+days
                total_days=total_days+count_days
                self.stack_prices.append(price)
                #print("total_days",total_days)
                self.stack_days.append(total_days)
                output.append(total_days)
                return total_days

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)