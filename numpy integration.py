import numpy as np

dice1 = np.random.randint(1, 7, size=10)
dice2 = np.random.randint(1, 7, size=10)
total = dice1 + dice2

print("Dice 1:", dice1)
print("Dice 2:", dice2)
print("Sum:   ", total)
