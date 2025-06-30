import matplotlib.pyplot as plt

days = ["Today", "Tomorrow", "Day-After Tomorrow"]
temperatures = [32, 30, 35]

plt.plot(days, temperatures, marker='o', label='Temperature')
plt.title('Temperature Trend Over the Week')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()
