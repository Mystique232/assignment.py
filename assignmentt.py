numbers = [2, 3, 6]

result = 1

for number in numbers:
    result = result * number

print(result)
# Question 2

items = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

items.sort(key=lambda x: x[-1])

print(items)
# Question 3

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = d1.copy()

for key, value in d2.items():
    result[key] = result.get(key, 0) + value

print(result)
# Question 4

n = int(input("Enter a number: "))

squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print(squares)
# Question 5

items = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

items.sort(key=lambda x: float(x[1]), reverse=True)

print(items)
# Question 6

numbers = {0, 1, 2, 3, 4}

# Iterate through the set
for number in numbers:
    print(number)

# Add a new item
numbers.add(5)

# Remove an item
numbers.remove(2)

print(numbers)