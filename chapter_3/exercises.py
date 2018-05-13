import matplotlib.pyplot as plt
import numpy as np
import math


# R-3.1
def plot_function(math_functions):
    x = np.arange(0, 1000, 0.1)
    fig, ax = plt.subplots()
    for f in math_functions:
        y = [f[0](x_element) for x_element in x]
        ax.plot(x, y, label=f[1])
        # ax.set_yscale('log') # enable or disable log scale

    plt.legend()
    plt.show()


# functions = [
#     (lambda x: 8 * x, '8x'),
#     (lambda x: 2 * x ** 2, '2x**2'),
#     (lambda x: x ** 3, 'x**3'),
#     (lambda x: 4.0 * x * math.log(x), '4*x*log(x)'),
# ]
#

# R-3.3
# 40 n^2 > 2n^3
# 20 n^2 > n^3
# 20 > n

# R-3.4 f(x) = 1

# functions = [
#     # (lambda x: 8 * x * math.log2(x), '8xlog(x)'),
#     (lambda x: x**4, 'aaa')
# ]
#
# plot_function(functions)
# R-3.6
# result = 0
# for entry in range(2, 102, 2):
#     result += entry
# n (n + 1) /2