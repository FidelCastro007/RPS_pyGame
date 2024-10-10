
#map

#Example 1
# List of temperatures in Celsius
celsius = [0, 20, 37, 100]

fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit)) 

#Example 1
prices = [100, 200, 300, 400, 500]

discounted_prices = map(lambda p:p*0.9, prices)
print(list(discounted_prices))  # Output: [90.0, 180.0, 270.0, 360.0, 450.0]


# Filter

#Example 1
users = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 25},
    {"name": "David", "age": 16},
]
adult_users = filter(lambda user: user["age"] >= 18, users)
print(list(adult_users))

#Example 2

logs = [
    "INFO: User logged in",
    "ERROR: Failed to load resource",
    "WARNING: Disk space low",
    "ERROR: Database connection lost",
    "INFO: User logged out",
]

# Using filter to extract error logs
error_logs = filter(lambda log:log.startswith('ERROR'), logs)

print(list(error_logs))

# Reduce

from functools import reduce

transactions = [
    {"id": 1, "amount": 100, "eligible_for_discount": True},
    {"id": 2, "amount": 200, "eligible_for_discount": False},
    {"id": 3, "amount": 150, "eligible_for_discount": True},
    {"id": 4, "amount": 300, "eligible_for_discount": False},
    {"id": 5, "amount": 250, "eligible_for_discount": True},
]

# Step 1: Filter out transactions where amount > 100
valid_transactions = filter(lambda t: t["amount"] > 100, transactions)

# Step 2: Apply a 10% discount to eligible transactions using a lambda function
discounted_amounts = map(
    lambda t: t["amount"] * 0.9 if t["eligible_for_discount"] else t["amount"], 
    valid_transactions
)

# Step 3: Sum up the total revenue using a lambda function
total_revenue = reduce(lambda acc, x: acc + x, discounted_amounts, 0)

print(total_revenue)

