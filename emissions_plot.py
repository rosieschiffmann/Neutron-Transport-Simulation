import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mean_emissions = []
error_emissions = []
neutron_numbers = np.array([100,1000,10000,50000,80000,100000])

file_list = ["neutron_penetration_emissions_100.csv", "neutron_penetration_emissions_1000.csv", "neutron_penetration_emissions_10000.csv", "neutron_penetration_emissions_50000.csv", "neutron_penetration_emissions_80000.csv","neutron_penetration_emissions_100000.csv"]
for file in file_list:
  df = pd.read_csv(file)
  average_emissions_temp = df['emissions'].mean()
  std_dev = df['emissions'].std()
  err_on_mean = std_dev / np.sqrt(len(df['emissions']))
  mean_emissions.append(average_emissions_temp)
  error_emissions.append(err_on_mean)


mean_emissions = np.array(mean_emissions)
error_emissions = np.array(error_emissions)

coeffs = np.polyfit(neutron_numbers, mean_emissions, deg=1)
poly = np.poly1d(coeffs)
x_fit = np.linspace(min(neutron_numbers), max(neutron_numbers), 100)
y_fit = poly(x_fit)

plt.errorbar(neutron_numbers, mean_emissions, yerr=error_emissions, fmt="none", label="Data", capsize=5)
plt.plot(x_fit, y_fit, color='red', linestyle='--', label=f"Fit: y = {coeffs[0]:.2e}x + {coeffs[1]:.2e}")
plt.ylabel("Mean Emissions, gCO2e")
plt.xlabel("Number of Neutrons")
plt.title("CO2e Emitted for Neutron Penetration Simulations")
plt.grid()
plt.legend()
plt.show()