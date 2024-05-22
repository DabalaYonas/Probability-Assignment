"""
Section 2
Group members
    Name                    ID
1.Bonsa Asafa			UGR/22810/13
2.Bsrat Mulugeta 		UGR/22871/13
3.Dabala Yonas			UGR/22688/13
4.Mekdes Haftu		    UGR/22830/13
5.Nazrawit Netsanet		UGR/23127/13
6.Simbo Fekadu		    UGR/22555/13
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon

scale = int(input("Input μ parameter value: "))
sample_size = 1000

print(f"Lambda(λ) value is {1/scale}:")

random_data = expon.rvs(scale=scale, size=sample_size)
plt.hist(random_data, bins=20, density=True) 

plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.title("Exponential Distribution (λ = {})".format(1/scale)) 
plt.grid(True)
plt.show()
