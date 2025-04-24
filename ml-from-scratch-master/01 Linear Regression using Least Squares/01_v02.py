# Making imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams['figure.figsize'] = (12.0, 9.0)
plt.rcParams['figure.figsize'] = (5.0, 4.0)


# Preprocessing Input data
data = pd.read_csv('data.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X, Y)
plt.show()

