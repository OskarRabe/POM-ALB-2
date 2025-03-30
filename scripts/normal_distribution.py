import random

import numpy as np

normal_distribution = np.random.normal(1.0, 0.1, 10000)

random_numbers = []
for number in normal_distribution:
    if 0.7 < number < 1.3:
        random_numbers.append(round(float(number), 2))
    if len(random_numbers) >= 12:
        break

print(random_numbers)

random_tasks = []
for i in range(4):
    num = random.randint(1, 12)
    random_tasks.append(num)

print(random_tasks)
