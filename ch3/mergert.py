import matplotlib.pyplot as plt
import math 

# Generate all x values
x = list(range(1, 100))

# Graph f(x^2) and f(7 * x * logx) to demonstrate the growth rate of merge sorting
plt.plot(x, [y*y for y in x])
plt.plot(x, [(7 * y) * math.log(y, 2) for y in x])
plt.show()
