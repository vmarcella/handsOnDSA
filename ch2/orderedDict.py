from collections import OrderedDict

# Create first ordered dictionary
od1 = OrderedDict()
od1['one'] = 1
od1['two'] = 2

# Create the second ordered dict, with reversed order
od2 = OrderedDict()
od2['two'] = 2
od2['one'] = 1

# Return false, because the order was not preserved
print(od1 == od2)

# Update the list into the ordered dictionary
some_list = [('three', 3), ('four', 4), ('five', 5)]
od1.update(some_list)
print(od1)

# turn the items stored within od1 into a sorted list and 
# then create a new sorted ordered dictionary
sorted_items = sorted(od1.items(), key= lambda item: item[1], reverse=True)
sorted_dict = OrderedDict(sorted_items)
print(sorted_dict)
