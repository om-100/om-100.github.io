#  question number 19
from functools import reduce

fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                              range(n - 2), [0, 1])

print("Fibonacci series upto 2:")
print(fib_series(2))