from collections import Counter

# Create a new counter instance with a str passed in as it's argument
new_counter = Counter('sequence')
print(new_counter)

# Update the counter object by providing it another iterable object
new_counter.update('eee')

# Return the most common items in order
print(new_counter.most_common())

# Subtract counts from items within the counter object
new_counter.subtract({'e': 2})
print(new_counter)
