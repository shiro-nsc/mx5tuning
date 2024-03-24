import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import csv
import os

# Function to convert hexadecimal to decimal
def hex_to_decimal(x):
    if isinstance(x, str):
        return int(x, 16)
    else:
        return x

# Function to find the air-fuel retio from the data frame in decimal using the factor
def find_air_fuel_ratio(x):
    y = 1470/(x*0.8+100)
    y = round(y,1)
    return y

filename = input("Enter a file name:")
#if os.path.exists(filename):

# Read the CSV file into a DataFrame
#df = pd.read_csv('sample_data/fuel_map.csv')
df = pd.read_csv(filename)

# Display in CSV
# print('here is in CSV')
# print(df)

# Convert hexadecimal to decimal for each element in the DataFrame
for column in df.columns:
    df[column] = df[column].apply(hex_to_decimal)

# store the data frame converted in decimal into fuel_map_decimal
fuel_map_decimal = df

# Display the DataFrame with hexadecimal data converted to decimal
# print('here is the data convereted to decimal')
# print(fuel_map_decimal)

# create air-fuel ratio map
for column in df.columns:
    df[column] = df[column].apply(find_air_fuel_ratio)

air_fuel_map = df

# Display the air-fuel map
# print('here is the air-fuel map')
# print(air_fuel_map)

# Convert DataFrame to NumPy array
air_fuel_array = df.values

# Display the DataFrame in array
print('here is air-fuel ratio stored in array')
print(air_fuel_array)



# air volume range from 0 to 15
air_volume = np.arange(16)

# RPM for x axis
# x = np.array([1024, 1536, 2048, 2560, 3072, 3584, 4096, 4608, 5120, 5632, 6144, 6656, 7168])
rpm_range = np.array([1024, 1536, 2048, 2560, 3072, 3584, 4096, 4608, 5120, 5632, 6144, 6656, 7168])
# air volume for y axis
# y = air_volume

# if x axis is reversed
# y = (air_volume)[::-1]

# Create a meshgrid for the x (RPM) and y (air volume) values
# X, Y = np.meshgrid(x, y)
X, Y = np.meshgrid(rpm_range, air_volume)

# air-fuel ratio for Z
Z = air_fuel_array

# air-fuel ratio for Z
# Z = (air_fuel_array)[::-1]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# Set labels and title
ax.set_xlabel('RPM')
ax.set_ylabel('Air volume')
ax.set_zlabel('Air-fuel ratio')
ax.set_title('3D Surface Plot of Air-fuel Ratio')

# Reverse the direction of the Z-axis
ax.set_zlim(ax.get_zlim()[::-1])
ax.set_xlim(ax.get_xlim()[::-1])

# Show color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()
