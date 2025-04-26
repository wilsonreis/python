import numpy as np
X = np.array([[ 1,  1,  1,  1,  1],
              [ 2,  5,  8, 11, 14],
              [ 3,  6,  9, 12, 15],
              [ 4,  7, 10, 13, 16]])
print("X.shape[0]:", X.shape[0])
I = np.identity(X.shape[0])  # Matriz identidad
print("I:", I)
'''
I: [    [1. 0. 0. 0.]
        [0. 1. 0. 0.]
        [0. 0. 1. 0.]
        [0. 0. 0. 1.]]

'''