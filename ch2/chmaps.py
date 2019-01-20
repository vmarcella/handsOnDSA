import collections

# Independent dictionaries
dict1 = {'a': 1, 'ruh': 2, 'sarin': 3}
dict2 = {'ruh': 30, 'tim': 40}

# Relates dict1 and dict2 to eachother
chainmap = collections.ChainMap(dict1, dict2)

# Print results
print(chainmap)
# Find a key, a, within all dicts stored inside the chainmap
print(chainmap['ruh'])
# Get a specific dictionary from the chainmap
print(chainmap.maps[0])
# Returns a values view???
print(chainmap.values())

# Create a new chainmap from the first one that 
# updates the value for ruh by placing a new dict
# at the front of the chain in order to give this new
# value the highest priority
cm2 = chainmap.new_child({'ruh': 40})
print('Printing ruh from the child chainmap')
# print the value of ruh
print(cm2['ruh'])
# print the parent chainmap of the current one
print(cm2.parents)
# print the current chainmap
print(cm2)
