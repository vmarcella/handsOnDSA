from collections import Counter

new_counter = Counter('sequence')
print(new_counter)

new_counter.update('eee')

print(new_counter.most_common())
