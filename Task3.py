# 3.	Произвести вычисления как в пункте 2, но с вычислением intercept. 
# Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно 
# (то есть изменение одного коэффициента не должно влиять на изменение другого во время 
# одной итерации).

import numpy as np
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

def mse_(B0, B1, ks = ks, zp = zp, n = len (zp)): 
    return np.sum((B0 + B1*zp - ks)**2)/ n
alpha = 5e-5

B0 = 0.1
B1 = 0.1
n = len (zp)
for t in range (2000000):
    B0 -= alpha * (2/n) * np.sum (B0 + B1 * zp - ks)
    B1 -= alpha * (2/n) * np.sum ((B0 + B1 * zp - ks) * zp)
    if t % 500000 == 0:
        print('B0 = {}'.format(B0), 'B1 = {}'.format(B1))

plt.scatter(zp, ks)
plt.plot(zp, B0 + B1 * zp)
plt.show()
