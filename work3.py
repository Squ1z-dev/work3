import numpy as np

grades =  np.random.randint(0,101, size=(100,3))
avarage = np.mean(grades, axis=1)

for i in range(100):
    print(f"student[{i+1}]: grades {grades[i]}, avg: {avarage[i]:.2f}")
