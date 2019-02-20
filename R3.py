import random

nsim = 10000
ptsInR1 = 0
ptsInR2 = 0

for i in range(0, nsim):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        ptsInR1 += 1
        if x <= 0.6:
            ptsInR2 += 1

vR3 = 4.*float(ptsInR2)/float(nsim) - float(ptsInR1)/float(nsim)
print(vR3)