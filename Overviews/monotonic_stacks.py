# %%


class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        days = 1
        
        while self.prices and self.prices[-1][0] <= price:
            days += self.prices.pop()[1]
        
        self.prices.append([price, days])

        return days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

stock_prices = [100, 80, 60, 70, 60, 75, 85]
spanner = StockSpanner()

for price in stock_prices:
    # print(f"Price: {price}, Span: {spanner.next(price)}")  
    spanner.next(price)
    print(f"Current Stack: {spanner.prices}")  # Print the current state of the stack


# %%
word = "Hello"
i = 2
insert = "a"
n = len(word)
print(word[:i] + insert +  word[i+1:n])

# %%
