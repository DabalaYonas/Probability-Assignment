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
from scipy.stats import norm
import numpy as np

mu = int(input("Enter mean(μ) value: "))
sigma = int(input("Enter standard deviation(σ): "))

x = np.linspace(mu - 3*sigma, mu + 3*sigma, 400) 
y = norm.pdf(x, mu, sigma)

plt.plot(x, y)

plt.xlabel("X-axis")
plt.ylabel("Probability Density")
plt.title("Gaussian Distribution (μ = {}, σ = {})".format(mu, sigma))

plt.grid(True)
plt.show()
