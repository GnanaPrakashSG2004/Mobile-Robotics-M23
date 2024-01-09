import numpy as np

amp = 6
mean = 15
std_dev = 19

num_points = 100
random_noise = 0.01 * np.random.randn(100)

x = np.linspace(-50, 50, num_points)
y = amp * np.exp(-(x - mean)**2 / (2 * std_dev**2)) + random_noise

data = np.column_stack((x, y))

np.save("./data/data_LM.npy", data)