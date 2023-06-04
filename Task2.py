# 2.	Посчитать коэффициент линейной регрессии при заработной плате (zp), 
# используя градиентный спуск (без intercept).
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], 
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. 

import numpy as np
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])


alpha = 1e-6

B1 = 0.1
n = len(zp)
for t in range (3000):
    B1 -= alpha * (2/n) * np.sum ((B1 * zp - ks) * zp)
    if t % 100 == 0:
        print ('B1 = {}'.format(B1))

plt.scatter(zp, ks)
plt.plot(zp, B1 * zp)
plt.show()
