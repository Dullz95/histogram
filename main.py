from numpy import *
import numpy as np
import matplotlib.pyplot as plt
values = str("values")
array = np.arange(0,21)
no_mean = np.mean(array)
std = round(np.std(array), 2)
vari = round(np.var(array), 2)
print(array)
print(std)
print(vari)

# activity

nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]

plt.hist(nums,bins)
plt.xlabel("nums")
plt.ylabel("bins")
plt.title("Histogram of nums against bins. ")
plt.show()