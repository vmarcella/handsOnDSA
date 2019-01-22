from collections import defaultdict

# Create a default dictionary, with int object being the default_factory function
dd = defaultdict(int)

word_list = ['red', 'blue', 'green', 'red', 'yellow', 'blue', 'red', 'green', 'green', 'red']

# iterate through the word list and add all values to the default dict regardless of if the keys
# are already there or not
for word in word_list:
    dd[word] += 1

print(dd)
