import numpy as np

growth_factors = np.array([0.7, 0.2, 0.5])
rainfall = np.array([[40, 50, 60],
                     [20, 35, 25],
                     [30, 40, 55]])

result = rainfall * growth_factors
print(result)
