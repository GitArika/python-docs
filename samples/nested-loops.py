import timeit
import random
import sys

# Optimized version
def optimized(u):
    SIZE = 10000
    INNER_LOOP = 100000
    random_index = random.randint(0, SIZE - 1)
    numbers = [sum(j % u for j in range(INNER_LOOP)) + random_index for i in range(SIZE)]
    return numbers[random_index]

# Test with a sample input
test_input = 7

# Time the functions
opt_time = timeit.timeit(lambda: optimized(test_input), number=1)

print(f"Optimized version: {opt_time:.2f} seconds")
