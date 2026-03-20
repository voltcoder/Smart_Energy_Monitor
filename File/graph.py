import matplotlib.pyplot as plt
import random

power_data = []

for i in range(20):
    current = random.uniform(0.5, 5)
    power = 230 * current
    power_data.append(power)

plt.plot(power_data)
plt.title("Power Consumption Trend")
plt.xlabel("Time")
plt.ylabel("Power (W)")
plt.show()
