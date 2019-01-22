import array
import sys

# Create an array and a list, composed of the same elements
int_array = array.array('i', range(10**6))
int_list = list(range(10**6))

# Check the percentage of memory used for the int_array compared to the int_list
# averages around 45% ??? Insane!
mem_percentage_used = 100 * (sys.getsizeof(int_array) / sys.getsizeof(int_list))
print(mem_percentage_used)

