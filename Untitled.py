#!/usr/bin/env python
# coding: utf-8

# In[8]:
# Hello i am shivam

import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E', 'F']
values = [5, 8, 9, 10, 4, 7]
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow']

plt.pie(values, explode=[0, 0.2, 0, 0, 0, 0], labels=labels, colors=colors, autopct='%0.1f%%', counterclock = False )
plt.title('Values')
plt.show()


# In[53]:


import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E', 'F']
values = [5, 8, 9, 10, 4, 7]

plt.bar(labels, values, color=['red', 'blue', 'yellow', 'black', 'orange', 'indigo'])


# In[37]:


def function(a = 0, b = 0):
    A = a
    B = b
    return (A, B)
s = function()
print(s)

import numpy as n

print(n.zeros((5, 4), int))

print([1, 2, 3] + [4, 5, 6])


# In[29]:


def int_to_english(num):
    if num < 0 or num > 1000:
        return "Number out of range"
    if num == 0:
        return "zero"
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        return tens[num // 10] + ("-" + ones[num % 10] if num % 10 != 0 else "")
    elif num < 1000:
        return ones[num // 100] + " hundred" + (" and " + int_to_english(num % 100) if num % 100 != 0 else "")
    else:
        return "Number out of range"

print(int_to_english(89))
# Output: "eighty-nine"

print(int_to_english(80))

print(int_to_english(100))
# Output: "one hundred"

print(int_to_english(567))
# Output: "five hundred and sixty-seven"

print(int_to_english(1001))
# Output: "Number out of range"


# In[42]:


def count_special_elements(lst):
    special_count = 0

    for i in range(len(lst)):
        to_check = lst[:i] + lst[i+1:]
        print(to_check)
        
        even_sum = sum(to_check[::2])
        odd_sum = sum(to_check[1::2])
        
        if even_sum == odd_sum:
            special_count += 1

    return special_count

A = [2, 1, 6, 4]
print(count_special_elements(A))
# Output: 1

B = [5, 5, 2, 5, 8]
print(count_special_elements(B))
# Output: 2


# In[43]:


import numpy as np

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.mat = np.zeros((rows, columns), dtype=int)

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def set_element(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.mat[i][j] = int(input(f'value at ({i}, {j}) : '))

    def __add__(self, other):
        try:
            return (np.add(self.mat, other.mat))
        except:
            return "Can't be Added"
        
    def __mul__(self, other):
        try:
            return (np.matmul(self.mat, other.mat))
        except:
            return "Can't be Multiply"

m1 = Matrix(2, 3)
m2 = Matrix(3, 2)

m1.set_element()
print()
m2.set_element()

add = m1+m2
mul = m1*m2

print(add)
print(mul)


# In[49]:


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.carts = []

    def add_cart(self, cart):
        self.carts.append(cart)

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        for i in range(quantity):
            self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
        
class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# Create some users
user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com")

# Create some items
item1 = Item("Shirt", 19.99, 10)
item2 = Item("Pants", 29.99, 5)

# Create some carts and add items to them
cart1 = Cart()
cart1.add_item(item1)
cart1.add_item(item2, quantity=2)
# cart1.remove_item(item2)

cart2 = Cart()
cart2.add_item(item1)

# Add carts to users
user1.add_cart(cart1)
user1.add_cart(cart2)
user2.add_cart(cart1)

# Print out some information
print("User 1:", user1.name)
for cart in user1.carts:
    print("Cart:")
    for item in cart.items:
        print("- ", item.name)

print("User 2:", user2.name)
for cart in user2.carts:
    print("Cart:")
    for item in cart.items:
        print("- ", item.name)


# In[26]:


class Pizza:
    def __init__(self, size, toppings, cheese):
        self.size = size
        self.toppings = toppings
        self.cheese = cheese

    def price(self):
        topping_cost = 0
        for topping in self.toppings:
            if topping in ["broccoli", "olives", "mushroom"]:
                topping_cost += 50
            else:
                topping_cost += 20
        cheese_cost = len(self.cheese) * 50
        size_cost = {"small": 50, "medium": 100, "large": 200}[self.size]
        return size_cost + topping_cost + cheese_cost

class Order:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.pizzas = []

    def order(self, size, toppings, cheese):
        pizza = Pizza(size, toppings, cheese)
        self.pizzas.append(pizza)

    def bill(self):
        total_cost = 0
        print("Customer Name: ", self.name)
        print("Customer ID: ", self.customer_id)
        print("Order Details:")
        for index, pizza in enumerate(self.pizzas):
            print("Pizza ", index+1, "Size: ", pizza.size, "Toppings: ", pizza.toppings, "Cheese: ", pizza.cheese, "Cost: ", pizza.price())
            total_cost += pizza.price()
        print("Total Cost: ", total_cost)

# Create an Order object and place some orders
order = Order("Alice", "1234")
order.order("small", ["corn", "tomato", "onion"], ["mozzarella"])
order.order("medium", ["capsicum", "olives"], ["mozzarella", "cheddar"])

# Generate the bill
order.bill()


# In[102]:


class FileNotFound(Exception):
    pass

class DifferentContent(Exception):
    pass

def compare_files(file1, file2):
    try:
        with open(file1, "r") as f1:
            content1 = f1.read()
    except FileNotFoundError:
        raise FileNotFound("File {} not found".format(file1))
    
    try:
        with open(file2, "r") as f2:
            content2 = f2.read()
    except FileNotFoundError:
        raise ("File {} not found".format(file2))

    if content1 != content2:
        raise DifferentContent("Files {} and {} do not have the same content".format(file1, file2))

    return True

def find_first_difference(file1, file2):
    try:
        with open(file1, "r") as f1:
            content1 = f1.read()
    except FileNotFoundError:
        raise FileNotFound("File {} not found".format(file1))
    
    try:
        with open(file2, "r") as f2:
            content2 = f2.read()
    except FileNotFoundError:
        raise FileNotFound("File {} not found".format(file2))

    if content1 != content2:
        for i, (c1, c2) in enumerate(zip(content1, content2)):
            if c1 != c2:
                print("First difference at position", i+1)
                break
    else:
        print("Files have the same content")

# Example usage
try:
    compare_files("file1.txt", "file2.txt")
    find_first_difference("file1.txt", "file2.txt")
except FileNotFound as e:
    print(e)
except DifferentContent as e:
    print(e)


# In[54]:


try:
    # attempt to open a file
    with open('example.txt', 'r') as f:
        
        contents = f.read()
        
        result = len(contents) / 0 # attempting to divide by zero
except FileNotFoundError:
    print("Oops! The file could not be found.")
    
except ZeroDivisionError:
    print("Oops! Division by zero is not allowed.")
    
finally:
    print("This code always runs, even if an exception was raised.")


# In[ ]:


def input_names():
    names = []
    mistakes = 0
    
    while True:
        name = input("Enter a name in the format 'Last Name, First Name' (or 'quit' to stop): ")
        
        if name.lower() == "quit":
            break
        
        # split the input into first and last names
        parts = name.split(",")
        
        if len(parts) != 2:
            print("Invalid input: Please enter a name in the format 'Last Name, First Name'.")
            mistakes += 1
        else:
            # remove leading/trailing whitespace from each part
            last_name = parts[0].strip()
            first_name = parts[1].strip()
            
            # check if the input was in the wrong order
            if " " in last_name or "," in first_name:
                # swap the first and last names
                first_name, last_name = last_name, first_name
                print("Input corrected to:", last_name + ",", first_name)
                mistakes += 1
            
            # add the name to the list
            names.append(last_name + ", " + first_name)
    
    # sort the list of names
    names.sort()
    
    # display the sorted names and the number of mistakes
    print("\nSorted names:")
    for name in names:
        print(name)
    
    print("Number of input mistakes:", mistakes)

# call the input_names function to start the program
input_names()


# In[57]:


def no_of_digits(num):
    i = 0
    while num > 0:
        num //= 10
        i+=1

    return i

def required_sum(num):
    i = no_of_digits(num)
    s = 0
    
    while num > 0:
        digit = num % 10
        num //= 10
        s += pow(digit, i)
        
    return s

num = int(input("Enter number:"))
s = required_sum(num)
     
if s == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


# In[71]:


s = 'sujal luhar'
if 'u' in s:
    S = list(s)
    for i in range(len(S)):
        if S[i] == 'u':
            S[i] = 'O'
    S = ''.join(S)
    print('yes')
print(S)


# In[80]:


s = 'Mr. Ed  ZZZ zzz(*&^%$)'

S = list(s)
for i, j in enumerate(S):
        if ord(j) in range(97, 123):
            S[i] = chr(ord(j) - 32)
        elif ord(j) in range(65, 91):
            S[i] = chr(ord(j) + 32)
ok = ''.join(S)
print(ok)


# In[94]:


with open('ok.txt', 'r') as f:
    while True:
        i = input('Enter  ').lower()
        if i == 'continue':
            for i in range(25):
                print(f.readline()[:-1])
        elif i == 'stop':
            break
        else:
            print("Enter from 'continue' and 'stop' only")
            


# In[1]:


# Open the file for reading
with open('filename.txt', 'r') as file:
    # Initialize variables
    lines = 0
    words = set()
    word_count = {}

    # Loop through each line in the file
    for line in file:
        # Increment the line counter
        lines += 1

        # Split the line into individual words
        line_words = line.split()

        # Add each word to the set of unique words
        for word in line_words:
            words.add(word)

            # Increment the word count in the dictionary
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Print the number of lines
    print("Number of lines:", lines)

    # Print the number of unique words
    print("Number of unique words:", len(words))

    # Print each word and its occurrence in the dictionary
    for word, count in word_count.items():
        print(word, count)


# In[2]:


import re

# Open the file for reading
with open('filename.txt', 'r') as file:
    # Initialize variables
    lines = 0
    words = set()
    word_count = {}

    # Loop through each line in the file
    for line in file:
        # Increment the line counter
        lines += 1

        # Split the line into individual words
        line_words = re.findall(r'\b\w+\b', line.lower())

        # Add each word to the set of unique words
        for word in line_words:
            words.add(word)

            # Increment the word count in the dictionary
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Print the number of lines
    print("Number of lines:", lines)

    # Print the number of unique words
    print("Number of unique words:", len(words))

    # Print each word and its occurrence in the dictionary
    for word, count in word_count.items():
        print(word, count)


# In[ ]:


# Open the input files for reading
with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    # Open the output file for writing
    with open('file3.txt', 'w') as file3:
        # Loop through each line in file1 and file2 simultaneously
        for line1, line2 in zip(file1, file2):
            # Write the lines to file3 alternately
            file3.write(line1)
            file3.write(line2)

        # Write any remaining lines from file1 to file3
        for line in file1:
            file3.write(line)

        # Write any remaining lines from file2 to file3
        for line in file2:
            file3.write(line)


# In[11]:


l = [1, 2, 3, 4, 13]
s = [13, 1, 2, 3, 13]

def sum_array(numbers):
    # Initialize variables
    total = 0
    skip_next = False

    # Loop through each number in the array
    for i in range(len(numbers)):
        # If the current number is 13, skip it and the next number
        if numbers[i] == 13:
            skip_next = True
        # If the previous number was 13, skip the current number
        elif skip_next:
            skip_next = False
        # Otherwise, add the current number to the total
        else:
            total += numbers[i]

    # Return the total
    return total
print(sum_array(s))


# In[12]:


class GTU:
    # Class variable
    cnt = 0

    def __init__(self, x, y):
        # Instance variables
        self.x = x
        self.y = y

        # Increment the class variable cnt
        GTU.cnt += 1

    def get_value(self):
        # Instance method
        return self.x + self.y

    def print_value(self):
        # Instance method
        print("x =", self.x)
        print("y =", self.y)
        print("x + y =", self.get_value())

# Example usage:
gtu1 = GTU(1, 2)
gtu2 = GTU(3, 4)

gtu1.print_value()  # Output: x = 1, y = 2, x + y = 3
gtu2.print_value()  # Output: x = 3, y = 4, x + y = 7

print("Total number of instances created:", GTU.cnt)  # Output: Total number of instances created: 2


# In[18]:


from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Maruti(Car):
    def drive(self):
        print("Maruti is being driven.")

class Santro(Car):
    def drive(self):
        print("Santro is being driven.")

# Example usage:
maruti = Maruti()
maruti.drive()  # Output: Maruti is being driven.

santro = Santro()
santro.drive()  # Output: Santro is being driven.


# In[16]:


# Take input from user for the amount (in cents)
amount = int(input("Enter amount (in cents): "))

# Calculate the number of quarters
quarters = amount // 25
amount = amount % 25

# Calculate the number of dimes
dimes = amount // 10
amount = amount % 10

# Calculate the number of nickels
nickels = amount // 5
amount = amount % 5

# Calculate the number of pennies
pennies = amount

# Print the result
if quarters > 0:
    if quarters == 1:
        print("1 quarter", end="")
    else:
        print(quarters, "quarters", end="")
if dimes > 0:
    if quarters > 0:
        print(", ", end="")
    if dimes == 1:
        print("1 dime", end="")
    else:
        print(dimes, "dimes", end="")
if nickels > 0:
    if quarters > 0 or dimes > 0:
        print(", ", end="")
    if nickels == 1:
        print("1 nickel", end="")
    else:
        print(nickels, "nickels", end="")
if pennies > 0:
    if quarters > 0 or dimes > 0 or nickels > 0:
        print(", ", end="")
    if pennies == 1:
        print("and 1 penny", end="")
    else:
        print("and", pennies, "pennies", end="")


# In[21]:


class MyCustomException(Exception):
    pass

def my_function(my_parameter):
    if my_parameter < 0:
        raise MyCustomException("my_parameter should be a positive integer")

try:
    my_function(-1)
except MyCustomException as e:
    print("Caught a MyCustomException:", e)

