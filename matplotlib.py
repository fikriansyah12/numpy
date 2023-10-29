import matplotlib.pyplot as plt
import numpy as np

# Create an array of evenly spaced numbers over a specified range (in this case, -4*pi to 4*pi)
x = np.linspace(-4*np.pi, 4*np.pi, 100)

# Calculate the sine function for each number in the array
y = np.sin(x)

# Create a plot
plt.plot(x, y)

# Set the labels for the x and y axes
plt.xlabel('x')
plt.ylabel('sin(x)')

# Set the title of the plot
plt.title('Plot of the sine function')

# Display the plot
plt.show()