import numpy as np

prices = np.array([10,20,30,40,50,])
discount = 10

final_prices = prices - (prices * discount/100)

print(final_prices)