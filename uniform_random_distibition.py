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
from matplotlib.patches import Rectangle
import random

min_value = int(input("Enter lower bound: "))
max_value = int(input("Enter upper bound: "))

while min_value >= max_value:
    max_value = int(input("Please Enter a value greater than lower bound: "))

count = int(input("Enter number random generated of values: "))

def calculate_graph_height(minValue, maxValue):
    diff = maxValue - minValue
    return (1/diff)

height = calculate_graph_height(min_value, max_value)

print("Probability density value is:", height)

x_label = f"Uniform distibuted value between {min_value} to {max_value}"
y_label = "probability density " + str(height)

title = "Uniform random distibution graph"

plt.figure()

plt.xlim(0, (max_value+20)) 
plt.ylim(0, (height))

width = max_value - min_value

rectangle = Rectangle(xy=(min_value, 0),
                      width = width, height = height,
                      color ='green', alpha = 0.4)

ax = plt.subplot()
ax.add_patch(rectangle)

uniform_random_numbers = [random.uniform(min_value, max_value) for i in range(count)]

print("Uniform Random Distribution numbers:", uniform_random_numbers)

plt.hist(uniform_random_numbers, color='gray')

plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)
plt.grid(True)
plt.show()

