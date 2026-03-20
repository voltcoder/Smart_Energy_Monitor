import random
import time

print("---- Smart Energy Monitor ----")

voltage = 230   # constant supply

for i in range(10):  # simulate readings
    current = random.uniform(0.5, 5)   # random current
    power = voltage * current          # P = V × I

    print(f"Voltage: {voltage} V")
    print(f"Current: {current:.2f} A")
    print(f"Power: {power:.2f} W\n")

    time.sleep(1)
