class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        count=1
        temp_arr=[]
        while self.stack and self.stack[-1]<=price:
            x=self.stack.pop()
            temp_arr.append(x)
            count+=1
        temp_arr=temp_arr[::-1]
        for k in temp_arr:
            self.stack.append(k)
        self.stack.append(price)
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)