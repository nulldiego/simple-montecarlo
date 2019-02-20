import random

nsim = 10000
ptsIn = 0

for i in range(0, nsim):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        ptsIn += 1

vR1 = 4.*float(ptsIn)/float(nsim)
print(vR1)