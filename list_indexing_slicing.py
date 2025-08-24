# %%
my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[1:3]) # output: ['banana', 'cherry']

my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[:2]) # output: ['apple', 'banana']
print(my_list[2:]) # output: ['cherry', 'date']


# [:3] means from the start to index 2 (exclusive)
sentence = "The quick brown fox jumps over the lazy dog"
first_word = sentence[:3]
print(first_word) # output: "The"

# [4:9] means from index 4 to index 8 (exclusive)
second_word = sentence[4:9]
third_word = sentence[10:15]
print(second_word) # output: "quick"
print(third_word) # output: "brown"


# Slicing a list to get every second element
# [::2] means every second element starting from index 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = numbers[::2]
print(odd_numbers) # output: [1, 3, 5, 7, 9]


# Extract Columns from 2D List
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
column = [row[1] for row in data] # This extracts the second column (index 1) from each row
print(column) # output: [2, 5, 8]

# Replacing a slice in a list
# This replaces elements at indices 1, 2, and 3 with new values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[1:4] = [10, 20, 30]
print(numbers) # output: [1, 10, 20, 30, 5, 6, 7, 8, 9]


# Inserting elements into a list using slicing
# This inserts elements at index 4 without removing any existing elements
numbers[4:4] = [40, 50]
print(numbers) # output: [1, 10, 20, 30, 40, 50, 5, 6, 7, 8, 9]

# If we have a list a = [0, 1, 2, 3, 4, 5], then:
a = [0, 1, 2, 3, 4, 5]
print(a[1:4]) # would return [1, 2, 3],
print(a[::2]) # would return every second element, [0, 2, 4],
print(a[::-1]) # would reverse the list, returning [5, 4, 3, 2, 1, 0].

# %%

# Reversing String 

my_string = "Hello, World!"
# Reversing the string using slicing
reversed_string = my_string[::-1]
print(reversed_string)  # Output: !dlroW ,olleH
reversed_str = my_string.reverse()

# %%
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_1 = [] # For ()
        parentheses_2 = [] # For {}
        parentheses_3 = [] # For []
        parentheses_1_open = False
        parentheses_2_open = False
        parentheses_3_open  = False

        for char in s:
            if char == "(":
                if parentheses_2_open or parentheses_3_open:
                    return False
                parentheses_1.append(char)

            elif char == "{":
                if parentheses_1_open or parentheses_3_open:
                    return False
                parentheses_2.append(char)

            elif char == "[":
                if parentheses_1_open or parentheses_2_open:
                    return False
                parentheses_3.append(char)

            elif char == ")":
                if parentheses_1:
                    parentheses_1.pop()
                else:
                    return False
            
            elif char == "}":
                if parentheses_2:
                    parentheses_2.pop()
                else:
                    return False

            elif char == "]":
                if parentheses_3:
                    parentheses_3.pop()
                else:
                    return False
            if len(parentheses_1) > 0:
                parentheses_1_open = True
            else:
                parentheses_1_open = False
            if len(parentheses_2) > 0:
                parentheses_2_open = True
            else:
                parentheses_2_open = False
            if len(parentheses_3) > 0:
                parentheses_3_open = True
            else:
                parentheses_3_open = False


        
        if not parentheses_1 and not parentheses_2 and not parentheses_3:
            return True
        else:
            return False
# %%
print("e" == "E")
s = "abBAcC"
print(s[0:1])
print(s[3:])
stack = []
for char in s:
    stack.append(char)
print(stack)
stack[-1]

# %%
from collections import deque
x = deque(maxlen=3)
x.append(1)

# %%
x = deque([0, 1, 2])
print(max(x))
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

stock_prices = [100, 80, 60, 70, 60, 75, 85, 80, 90, 100, 50, 60]
spanner = StockSpanner()

for price in stock_prices:
    # print(f"Price: {price}, Span: {spanner.next(price)}")  
    spanner.next(price)
    print(f"Current Stack: {spanner.prices}")  # Print the current state of the stack
