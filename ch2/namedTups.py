from collections import namedtuple

# Create a named tuple space, with values being x, y, and z coordinates
space = namedtuple('space', 'x y z')

s1 = space(x=2.0, y=3.0, z=10)
print(s1)

# print a specific value from the tuple 
print(s1.x)

# Convert a coordinate list into a named space tuple using the ._make function provided
# by namedtuple
coordinate_list = [4, 10, 30]
s2 = space._make(coordinate_list)
print(s2)

# Returns a named tuple as a ordereddictionary where the fields are ordered by the order
# they were specified in upon creation
print(s1._asdict())

# Return a new instance of space where the x value has been modified
print(s1._replace(x=10))

# Print all of the fields within the named tuple
print(space._fields)
