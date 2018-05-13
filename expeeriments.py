import numpy as np

def reshape(x):
  """return x_reshaped as a flattened vector of the multi-dimensional array x"""

  x_reshaped = x.flatten()
  return x_reshaped



aaa = np.ones((28, 28), int)
print(aaa)
print('8888888888888888888888888888888888')
reshaped = reshape(aaa)
print(reshaped)