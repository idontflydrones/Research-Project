
import pandas as pd
import matplotlib.pyplot as plt

# Read the scaled dataset
D4 = pd.read_csv("scaled_state_metrics_2025.csv")

# Four scaled indicators
x = D4["Fs_scaled"]
y = D4["Es_scaled"]
z = D4["Gs_scaled"]
color = D4["Ps_scaled"]

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

points = ax.scatter(x, y, z, c=color)

# Label the axes
ax.set_xlabel("Flex-Fuel Vehicles (Fs)")
ax.set_ylabel("E85 Stations (Es)")
ax.set_zlabel("Gasoline Consumption (Gs)")

# Color represents gasoline price
colorbar = fig.colorbar(points, ax=ax, pad=0.1)
colorbar.set_label("Gasoline Price (Ps)")

ax.set_title("4D Point Cloud of E85 Indicators")

plt.show()
