from sklearn import preprocessing
import numpy as np
from sklearn.datasets import fetch_california_housing

california_housing = fetch_california_housing(as_frame=True)
#print(california_housing.DESCR)
print(type(california_housing))

x_array = np.array(california_housing.data['HouseAge'])
print("HouseAge array: ",x_array)

normalized_arr = preprocessing.normalize([x_array])
print("Normalized HouseAge array: ",normalized_arr)